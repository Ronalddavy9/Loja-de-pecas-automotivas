from flask import Flask, render_template, request

app = Flask(__name__)

# Dados das peças
pecas = [
    {"nome": "Pneu aro 16 Firestone", "descricao": "Pneu para carros de passeio aro 16", "preco": "R$ 350,00", "imagem": "https://i.zst.com.br/thumbs/12/4/16/767578282.jpg"},
    {"nome": "Bateria Moura 60Ah", "descricao": "Bateria para automóveis 60Ah", "preco": "R$ 450,00", "imagem": "https://lojaodasbaterias.com/wp-content/uploads/2021/08/M60GE.png"},
    {"nome": "Filtro de óleo Mann", "descricao": "Filtro de óleo para motor 1.6", "preco": "R$ 30,00", "imagem": "https://images.cws.digital/produtos/gg/66/85/filtro-de-oleo-lubrificante-1088566-1622583775617.jpg"},
    {"nome": "Amortecedor dianteiro Cofap", "descricao": "Amortecedor dianteiro para diversos modelos", "preco": "R$ 250,00", "imagem": "https://images.tcdn.com.br/img/img_prod/150352/par_amortecedor_dianteiro_honda_hrv_original_cofap_novo_gp33285_gp33286_8477_1_20200907084217.jpg"},
    {"nome": "Disco de freio Fremax", "descricao": "Disco de freio ventilado para carros populares", "preco": "R$ 180,00", "imagem": "https://berko.com.br/wp-content/uploads/2020/11/DISCO_FREIO_BD7829.jpg"},
    {"nome": "Pastilha de freio Bosch", "descricao": "Pastilha de freio para carros europeus", "preco": "R$ 120,00", "imagem": "https://a-static.mlcdn.com.br/1500x1500/jogo-pastilha-freio-dianteira-bosch-saveiro-robust-1-6/naska2/npfdb-010/ce5725000b9a0e6d35f0cd0da3b501fa.jpeg"},
    {"nome": "Vela de ignição NGK", "descricao": "Vela de ignição para motores 1.0", "preco": "R$ 40,00", "imagem": "https://36322.cdn.simplo7.net/static/36322/sku/velas-vela-de-ignicao-ngk-pfr6j-11-avenger-stealth-3000-diamant-galant-pajero-unitario--p-1607539423409.png"},
    {"nome": "Correia dentada Gates", "descricao": "Correia dentada para motores 1.6", "preco": "R$ 80,00", "imagem": "https://cornelio-maverick-produtos.s3.amazonaws.com/loja/imagens/full/gatess.png"},
    {"nome": "Radiador Valeo", "descricao": "Radiador para carros nacionais", "preco": "R$ 300,00", "imagem": "https://images.tcdn.com.br/img/img_prod/796938/radiador_vw_gol_g5_g6_1_0_1_6_c_ar_valeo_30247_1_85bfc2641dd23268d800cca61af5c8a2.jpg"},
    {"nome": "Lâmpada Philips H4", "descricao": "Lâmpada halógena para farol", "preco": "R$ 25,00", "imagem": "https://images.tcdn.com.br/img/img_prod/793827/lampada_farol_titan_150_philips_h4_fit_203_1_e9c8e1d94f604f296d254eb301ce8e7b.jpg"},
    {"nome": "Bomba de combustível Bosch", "descricao": "Bomba de combustível para injeção eletrônica", "preco": "R$ 280,00", "imagem": "https://images.tcdn.com.br/img/img_prod/734304/bomba_de_combustivel_universal_bosch_f000te0103_vw_ford_fiat_gm_toyota_honda_3bar_gas_refil_103_bosc_715_1_20200626170638.jpeg"},
    {"nome": "Sensor de oxigênio Denso", "descricao": "Sensor de oxigênio para controle de emissões", "preco": "R$ 180,00", "imagem": "https://m.media-amazon.com/images/I/5167siIg+nL._AC_SX300_SY300_.jpg"},
    {"nome": "Sensor de temperatura Delphi", "descricao": "Sensor de temperatura para sistemas de arrefecimento", "preco": "R$ 60,00", "imagem": "https://a-static.mlcdn.com.br/1500x1500/sensor-de-temperatura-delphi-std00004-gm-celta-cod-8575/dbauto/8575/f0d044f65666e355d63845046efd975c.jpeg"},
    {"nome": "Jogo de tapetes automotivos", "descricao": "Tapetes universais para carros", "preco": "R$ 50,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_697456-MLB49151486352_022022-O.webp"},
    {"nome": "Calota esportiva R13", "descricao": "Calota esportiva para rodas aro 13", "preco": "R$ 30,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_2X_967152-MLB72555989058_112023-F.webp"},
    {"nome": "Engate para reboque", "descricao": "Engate para reboque universal", "preco": "R$ 200,00", "imagem": "https://31b93296e4855c6e.cdn.gocache.net/loja/imagens/full/engate-reboque-enforth-fixo.png"},
    {"nome": "Escapamento esportivo", "descricao": "Escapamento esportivo para carros esportivos", "preco": "R$ 500,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_954754-MLB28107285685_092018-O.webp"},
    {"nome": "Kit de embreagem Luk", "descricao": "Kit de embreagem para carros de passeio", "preco": "R$ 600,00", "imagem": "https://images.tcdn.com.br/img/img_prod/945233/kit_embreagem_luk_original_619301500_104417_1_8622370e5353c8d0390d9fc5102650ac.png"},
    {"nome": "Farol auxiliar LED", "descricao": "Farol auxiliar de LED para off-road", "preco": "R$ 150,00", "imagem": "https://www.innovalite.com.br/wp-content/uploads/2021/04/IL6007-1.jpg"},
    {"nome": "Central multimídia Pioneer", "descricao": "Central multimídia com tela touch", "preco": "R$ 800,00", "imagem": "https://m.media-amazon.com/images/I/51nmvAiORhL.__AC_SX300_SY300_QL70_ML2_.jpg"},
    {"nome": "Tapete de porta-malas", "descricao": "Tapete de borracha para proteção do porta-malas", "preco": "R$ 70,00", "imagem": "https://alfabetoauto.com.br/image/cache/webp/800x800/catalog/elri-tapetes/product_image-1052992063-1.webp"},
    {"nome": "Retrovisor externo completo", "descricao": "Retrovisor externo com regulagem elétrica", "preco": "R$ 350,00", "imagem": "https://stgecomm.blob.core.windows.net/imagesprod2/0430958_espelho-retrovisor-externo-volkswagen-4150-delivery-lado-direito-eletrico-completo-volkswagen-23b857_450.jpeg"},
    {"nome": "Aditivo para radiador", "descricao": "Aditivo concentrado para sistemas de arrefecimento", "preco": "R$ 20,00", "imagem": "https://images.tcdn.com.br/img/img_prod/1039962/aditivo_para_radiador_ipiranga_pronto_para_uso_1l_1213_1_82c0fe207d8e49cedb8c7878853edb7c.jpg"},
    {"nome": "Cabo de vela MSD", "descricao": "Cabo de vela de alto desempenho", "preco": "R$ 120,00", "imagem": "https://acdn.mitiendanube.com/stores/001/387/760/products/projeto-remover-fundo-2024-01-19t152417-509-49b5d1939497b2fba717056890989349-640-0.webp"},
    {"nome": "Caixa de direção TRW", "descricao": "Caixa de direção para veículos utilitários", "preco": "R$ 400,00", "imagem": "https://images.tcdn.com.br/img/img_prod/150352/7861_0_20200305081708.jpg"},
    {"nome": "Aerofólio esportivo", "descricao": "Aerofólio traseiro para estilização esportiva", "preco": "R$ 180,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_805372-MLB49755027579_042022-O.webp"},
    {"nome": "Kit de molas esportivas", "descricao": "Kit de molas rebaixadas para melhor performance", "preco": "R$ 300,00", "imagem": "https://cdn.spiritshop.com.br/dubstore/image/cache/data/up_system/product-63/001-Eibach-quatro-molas-caixa-vermelha-2020-860x860.jpg"},
    {"nome": "Tapete personalizado", "descricao": "Tapete personalizado com logo de montadora", "preco": "R$ 80,00", "imagem": "https://m.media-amazon.com/images/I/71WdJyl7EDL.__AC_SY300_SX300_QL70_ML2_.jpg"},
    {"nome": "Kit de rodas aro 17", "descricao": "Kit de rodas esportivas aro 17 com pneus", "preco": "R$ 2000,00", "imagem": "https://www.fullpneus.com.br/wp-content/uploads/2023/07/roda-aro-17-tsw-nurbugring.jpg"},
    {"nome": "Sensor de estacionamento", "descricao": "Sensor de estacionamento com display", "preco": "R$ 150,00", "imagem": "https://s3-sa-east-1.amazonaws.com/loja2/f1a597194a4790b7827aa7e34ae1d22a.png"},
    {"nome": "Engrenagem de câmbio", "descricao": "Engrenagem para câmbio manual", "preco": "R$ 90,00", "imagem": "https://acdn.mitiendanube.com/stores/794/919/products/agd_3583-21-dafade3c60203f3daa15269104762655-480-0.webp"}
]


@app.route('/')
def index():
    query = request.args.get('query')
    if query:
        pecas_filtradas = [peca for peca in pecas if query.lower() in peca['nome'].lower()]
    else:
        pecas_filtradas = pecas
    return render_template('index.html', pecas=pecas_filtradas, query=query)

@app.route('/comprar/<nome>', methods=['GET', 'POST'])
def comprar(nome):
    # Encontrar a peça correspondente pelo nome
    peca = next((peca for peca in pecas if peca['nome'] == nome), None)
    if peca:
        if request.method == 'POST':
            # Lógica para processar o formulário de compra aqui
            # Exemplo: capturar dados do formulário e processar o pagamento, etc.
            return "Compra realizada com sucesso!"
        # Renderiza a página de compra com os detalhes da peça
        return render_template('compra.html', peca=peca)
    else:
        return "Página não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
