SECRET_KEY = ''
PUBLIC_KEY = ''
INTERVAL = 1800 # inteval is in seconds

SOURCE = {
    'whattomine': {
        "url": "https://whattomine.com/coins.json?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=0&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=6&adapt_q_1080=0&adapt_q_1080Ti=2&factor%5Beth_hr%5D=70.0&factor%5Beth_p%5D=280.0&factor%5Bgro_hr%5D=116.0&factor%5Bgro_p%5D=420.0&factor%5Bx11g_hr%5D=39.0&factor%5Bx11g_p%5D=340.0&factor%5Bcn_hr%5D=1660.0&factor%5Bcn_p%5D=280.0&eq=true&factor%5Beq_hr%5D=4600.0&factor%5Beq_p%5D=1300.0&factor%5Blrev2_hr%5D=128000.0&factor%5Blrev2_p%5D=380.0&factor%5Bns_hr%5D=2800.0&factor%5Bns_p%5D=380.0&factor%5Blbry_hr%5D=920.0&factor%5Blbry_p%5D=380.0&factor%5Bbk14_hr%5D=8700.0&factor%5Bbk14_p%5D=420.0&factor%5Bpas_hr%5D=3400.0&factor%5Bpas_p%5D=420.0&factor%5Bskh_hr%5D=95.0&factor%5Bskh_p%5D=380.0&factor%5Bn5_hr%5D=150.0&factor%5Bn5_p%5D=380.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.22&sort=Difficulty&volume=0&revenue=current&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=abucoins&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate",
        "rig_ids" : "20890", #rig id separated by coma ,
        "profitable_key" : "btc_revenue" # you can change profitabily base on whattomine keys. NOTE you can only choose integer value
    }
}
