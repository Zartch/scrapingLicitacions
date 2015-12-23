# -*- coding: utf-8 -*-
import re
import scrapy
from licitGene.items import Contractant,Contracte,Lot,Empresa
import logging


logger = logging.getLogger('mycustomlogger')
handler1 = logging.FileHandler('Errors.log')
handler1.setLevel(logging.WARNING)
logger.addHandler(handler1)


#recibe una cadena tipo 'bla 33.156,22 bla' y devuelve 33156.22
#si encontrara una cadena tipo "40.125,44 € IVA inclòs (21,00%)" devolveria [40125.44,21.00]
def get_euros(str):
    aux = str.replace(".","")
    aux = aux.replace(",",".")
    aux = re.findall(r'\d+\.*\d*', aux)
    return aux

class LicitacionsSpider(scrapy.Spider):
    items = []
    name = "licitacionsGene"
    allowed_domains = ["contractaciopublica.gencat.cat"]
    start_urls = [
        #"https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/search.pscp?reqCode=searchDcan&advancedSearch=false&lawType=2",
        'https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=12886334&advancedSearch=false&lawType=2&reqCode=viewDcan&',
   ]

    def parse(self, response):
        logging.info('****start crawling***')
        #SCRAPEA SOLO UNA PAGINA (el enlace tiene que ser directamente la pagina)
        try:
            yield scrapy.Request(response.url, callback=self.parse_dir_contents)
        except Exception, e:
            logging.exception(e)

        # #SCRAPEA SOLO UNA PAGINA (EL PRIMER ENLACE) de una pagina que liste paginas
        # try:
        #     url = response.urljoin(response.css('#contingut dl a').xpath('@href').extract()[0])
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)
        # except Exception, e:
        #     logging.exception(e)

        #Cadauno de los links de la pagina a los que hay que enviar el parser
        # for href in response.css('#contingut dl a').xpath('@href').extract():
        #     try:
        #         url = response.urljoin(href)
        #         logging.info('****crawling***'+ url)
        #         yield scrapy.Request(url, callback=self.parse_dir_contents)
        #     except Exception as e:
        #         logger.error(str(e) + response.urljoin(href))
        #         logging.warning(e)
        # next_page = response.css("#paginacio .PagingTag a")[-2].xpath('@href').extract()[0]
        # if next_page:
        #     url = response.urljoin(next_page)
        #     logging.info('****NEXT PAGE***'+ url)
        #     yield scrapy.Request(url, self.parse)


        return

    def parse_dir_contents(self, response):
        #Contractant
        contractant = Contractant()
        contractant['organdeC'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[0].strip()
        contractant['primary'] = contractant['organdeC']
        yield contractant

        #Contracte
        contracte = Contracte()
        contracte['contractant'] = contractant['organdeC']
        contracte['url'] = response.url
        contracte['codiexpedient'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[1].strip()
        contracte['tipusexpedient'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[2].strip()
        contracte['tipuscontracte'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[3].strip()
        #logging.info(response.css('#denominacio-contracte dd').xpath('text()').extract()[0].strip())
       # logging.info('***PASA***')
        #pot existir o no
        aux = response.css('#denominacio-contracte dt').xpath('text()').extract()[4].strip()

        #variable per saber si el procediment està al 4 o al 5
        proximaInfo = 4

        if aux == "Subtipus de contracte:":
            contracte['subtipuscontracte'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[4].strip()
            proximaInfo = 5

        contracte['procediment'] = response.css('#denominacio-contracte dd').xpath('text()').extract()[proximaInfo].strip()

        #Dades del Contracte
        contracte['descripcio'] = response.css(".dades-contracte dl dd").xpath('text()').extract()[0]
        try:# Algun sense import https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=13133550&advancedSearch=false&lawType=2&reqCode=viewDcan&
            contracte['presupostSENSEIVA'] = get_euros(response.css(".dades-contracte dl dd span").xpath('text()').extract()[0])[0]
        except IndexError:
            pass
        a = get_euros(response.css(".dades-contracte dl dd span").xpath('text()').extract()[1])
        try:
            contracte['presupostIVA'] = a[0]
            contracte['percentIVA'] = a[1]
        except IndexError:
            #https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=13041202&advancedSearch=false&lawType=2&reqCode=viewDcan&
            contracte['presupostIVA'] = get_euros(response.css(".dades-contracte dl dd").xpath('text()').extract()[3])[0]
            pass


        #Pot ser 'Termini' o 'durada' "1any" o "11/11/11 - 31/11/11"
        contracte['durada'] = u" ".join(response.css(".dades-contracte dl dd").xpath('text()').extract()[4].split())
        contracte['primary'] = contracte['url']


        #Diferencies segons la informació
        #(5 camps)https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=2787510&advancedSearch=false&lawType=2&reqCode=viewPcan&
        #(10 camps)https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=13115121&advancedSearch=false&lawType=2&reqCode=viewPcan&
        #(6 Camps)https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=13123417&advancedSearch=false&lawType=2&reqCode=viewPcan&%27

        #Els seguents camps poden estar o no
        # contracte['ambitgeografic'] , contracte['observacions']
        # contracte['valorestimat'] , contracte['subhasta'] , contracte['oberturapliques']

        #response.css(".dades-contracte dl")[X].css("dd").extract()
        # X == 0 -> Dades del contracte
        # X == 1 -> Dada de publicació + IMG
        # X == 2 -> Dades de l'adjudicació

        def tractaCamps(ambitgeografic, dt, dd):
            var = ''
            if dt == 'Observacions:':
                var = 'observacions'
            elif dt == 'Valor estimat del contracte:':
                var = 'valorestimat'
            elif dt == u'Subhasta electr\xf2nica':
                var = 'subhasta'
            elif dt == u'Obertura de pliques:':
                var = 'oberturapliques'
            elif dt == u'\xc0mbit geogr\xe0fic:':
                var = 'ambitgeografic'

            if var != '':
                ambitgeografic[var] = dd


        #Agafem la llista de camps de dades del contracte y la recorrem a la inversa fins arribar al 4 y las pasem
        ncamps = len(response.css(".dades-contracte dl")[0].css("dt").xpath('text()')) - 1
        while ncamps > 0:
            dt = response.css(".dades-contracte dl")[0].css("dt").xpath('text()')[ncamps].extract()
            dd = response.css(".dades-contracte dl")[0].css("dd").xpath('text()')[ncamps].extract()
            tractaCamps(contracte, dt, dd)
            ncamps -= 1
        yield  contracte
        #response.css(".dades-contracte dl dt").xpath('text()').extract()[4].split()

        #logging.info('***2***')
        #Dades de l'adjudicació
        lot = Lot()
        empresa = Empresa()
        try:
            #utilitzar losts
            #comencém per el ultim lot i arribem fins el 0
            numLot = len(response.css(".grup-lot")) -1

            while numLot >= 0:
                lot['primary'] = response.url
                lot['url'] = response.url
                lot['numero'] = numLot #int(re.findall(r'\d+', response.css(".grup-lot")[numLot].css("dd").xpath("text()")[0].extract()))
                lot['descripcio'] = response.css(".grup-lot")[numLot].css("dd").xpath("text()")[1].extract()
                lot['data'] = response.css(".grup-lot")[numLot].css("dd").xpath("text()")[2].extract()
                lot['cpv'] = response.css(".grup-lot")[numLot].css("dd").xpath("text()")[4].extract()
                #A partir de aqui el Lot pot quedar desert o indicar la empresa adjudicataria del lot
                #logging.info('***Comprobacio lots 2***' + str(numLot))
                if response.css(".grup-lot")[numLot].css("dt").xpath("text()")[4].extract() == 'Lot desert':
                    lot['desert'] = 'True'
                else:
                    lot['desert'] = 'False'
                    #lot['numofertes'] = response.css(".grup-lot")[numLot].css(".dades-empresa dd").xpath("text()")[4].extract()
                    try:
                        lot['importiva'] = get_euros(response.css(".grup-lot")[numLot].css(".dades-empresa dd").xpath("text()")[3].extract())[0]
                    except IndexError:
                        lot['importiva'] = get_euros(response.css(".grup-lot")[numLot].css("dd").xpath("text()")[4].extract())[0]
                    try:
                        lot['importsenseiva'] = get_euros(response.css(".grup-lot")[numLot].css(".dades-empresa dd").xpath("text()")[4].extract())[0]
                    except IndexError:
                        pass
                    #logging.info('***Comprobacio lots 3***' + str(numLot))
                    #Si el lot no ha quedat desert, agafem la empresa adjudicataria

                    empresa['denominacio'] = response.css(".grup-lot")[numLot].css(".dades-empresa dd")[0].xpath("text()").extract()[0]
                    empresa['nacionalitat'] = response.css(".grup-lot")[numLot].css(".dades-empresa dd")[1].xpath("text()").extract()[0]
                    try:
                        logging.info('***Comprobacio lots TRY***' + str(numLot))
                        empresa['nif'] = response.css(".grup-lot")[numLot].css(".dades-empresa dd")[2].xpath("text()").extract()[0]
                        lot['asignacio'] = empresa['nif']
                    except IndexError:
                        logging.info('***Comprobacio lots except***' + str(numLot))
                        empresa['nif'] = "Sense Info"

                numLot -= 1
                #logging.info('***Lots!***')


        except IndexError:
            #logging.info('***SenseLots***')
            #no te lots, utilitzem el normal
            #response.css(".dades-contracte dl")[2] - > Dades adjudicacio
            lot['url'] = response.url
            lot['numero'] = 0
            lot['descripcio'] = 'Unic lot'
            lot['desert'] = 'False'
            lot['data'] = ''
            lot['cpv'] = ''
            try:
                lot['importiva'] = get_euros(response.css(".dades-contracte dl")[2].css(".dades-empresa dd")[3].xpath("text()").extract()[0])[0]
            except IndexError:
                try:
                    lot['importiva'] = get_euros(response.css(".dades-contracte dl")[2].css("dd")[3].extract())[0]
                except IndexError:
                    try:
                        lot['importiva'] = get_euros(response.css(".dades-contracte dl")[3].css("dd")[3].extract())[0]
                    except IndexError:
                        #https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?idDoc=13212142&advancedSearch=false&lawType=2&reqCode=viewDcan&
                        pass

            try:
                lot['importsenseiva'] = get_euros(response.css(".dades-contracte dl")[2].css(".dades-empresa dd")[4].xpath("text()").extract())
            except:
                pass
            
            #Creem la empresa y li asignem el lot
            try:
                empresa['denominacio'] = response.css(".dades-contracte dl")[2].css(".dades-empresa dd")[0].xpath("text()").extract()[0]
                empresa['nacionalitat'] = response.css(".dades-contracte dl")[2].css(".dades-empresa dd")[1].xpath("text()").extract()[0]
            except IndexError:
                #https://contractaciopublica.gencat.cat/ecofin_pscp/AppJava/awardnotice.pscp?reqCode=viewDcan&idDoc=13158355&version=13158355&lawType=2
                empresa['denominacio'] = response.css(".dades-contracte dl")[3].css(".dades-empresa dd")[0].xpath("text()").extract()[0]
                empresa['nacionalitat'] = response.css(".dades-contracte dl")[3].css(".dades-empresa dd")[1].xpath("text()").extract()[0]
            try:
                #En algún exemple m'he trobat que no hi ha nif de la empresa
                empresa['nif'] = response.css(".dades-contracte dl")[2].css(".dades-empresa dd")[2].xpath("text()").extract()[0]
                lot['asignacio'] = empresa['nif']
            except IndexError:
                empresa['nif'] = "Sense Info"


        #logging.info('***Yeld LOT***')
        lot['primary'] = response.url + '_lot_' + str(lot['numero'])
        yield lot

        #logging.info('***Yeld Empresa***'+ str(empresa['nif']) )
        empresa['primary'] = empresa['nif']
        yield empresa
        #items.append(lot)
        #items.append(empresa)


