import numpy as np
import pandas as pd

def decay(ce_strike,pe_strike, client, ce, pe, date1, date2, df ):
    try:
        call = ce_strike
        put = pe_strike

        symbol_ce = ce + str(call) + '.00'
        symbol_pe = pe + str(put) + '.00'

        scrip_code = df.loc[df['Name'] ==  symbol_ce].iloc[0]['Scripcode']
        df_ce = client.historical_data('N','d',scrip_code,'5m',date1, date2)

        scrip_code = df.loc[df['Name'] ==  symbol_pe].iloc[0]['Scripcode']
        df_pe = client.historical_data('N','d',scrip_code,'5m',date1, date2)



        df_ = pd.DataFrame(
        {'timestamp': df_ce['Datetime'] ,
         'strangle':  df_ce['Close'] +  df_pe['Close'],
         'volume':    df_ce['Volume'] +  df_pe['Volume']
        })

        df_['vwap'] = (np.cumsum(df_.volume * df_.strangle) / np.cumsum(df_.volume))
        #df_['error'] = abs(df_['strangle'] - df_['vwap'])
        #df_['2-sigma'] = df_['vwap'] + 2 * (np.cumsum(df_.error) / np.size(df_.error))


        plt.subplots(figsize=(20, 10))
        sns.lineplot(data=df_, x=df_['timestamp'], y=df_['strangle'], label = 'strangle_value')
        sns.lineplot(data=df_, x=df_['timestamp'], y=df_['vwap'],  label = 'VWAP')
        plt.xticks(rotation=45)
        plt.show()


    except Exception as ex:
        print(ex)
        
        
    #globals().update(locals())
    
    return df_