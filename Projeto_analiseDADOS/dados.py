import pandas as pd

try:
    affiliates_df = pd.read_csv('affiliates.csv')
except FileNotFoundError as e:
    print("Arquivo CSV dos afiliados não encontrado:", e)
    exit()

limits = {
    120: 8,
    286: 16,
    310: 35,
    444: 42,
    500: 50
}


payments = []
porcentagens_qualificadoras = []

for index, row in affiliates_df.iterrows():
    payment = row['payment']
    
  
    porcentagem = next((valor_porcentagem for limite, valor_porcentagem in limits.items() if payment <= limite), 50)
    
  
    final_payment = (porcentagem / 100) * payment
    
    payments.append(final_payment)
    porcentagens_qualificadoras.append(porcentagem)


affiliates_df['porcentagem_qualificadora'] = porcentagens_qualificadoras
affiliates_df['pagamento_final'] = payments


print("Relatório de pagamentos finais:")
print(affiliates_df)
