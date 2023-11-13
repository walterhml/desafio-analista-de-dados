<div>
   <img src=".github/logo-mini.png" height="30">
</div>

# Desafio de análise de dados

## Recursos
- Banco de dados com acesso a clientes e apostas.
```
Postgresql
Host: 144.22.211.147
Port: 5436
User: bear
Password: dev!!!00
Database: upbet
```
- CSV de pagamentos dos afiliados.
    [Baixe aqui](/affiliates.csv)


## Objetivos
- Encontrar a porcentagem para calcular o valor de acréscimo.
- Calcular a soma total de apostas do cliente de cada afiliado do arquivo CSV.
- Utilizando os totais das apostas e os dados da tabela limites, determinar a porcentagem aplicada ao pagamento final.

## Cálculo do pagamento

`(Porcentagem encontrada / 100) * (Coluna pagamentos do csv)`

### Exemplo
```
Para uma soma total de apostas de R$340, a porcentagem aplicada será de 25%.
O valor está dentro do limite de R$400.
```

| Valor  | Porcentagem  |
|--------|--------------|
| 100    | 10%          |
| 200    | 15%          |
| 300    | 20%          |
| 400    | 25%          |
| 500    | 30%          |

#### * Valores maiores que R$500 é aplicado 50%

## Resultado final
### Dados essenciais no relatório
```
ID de afiliado (affiliate_id) - CSV
Valor do pagamento - CSV
Soma das apostas do cliente - Banco de dados
Porcentagem do acréscimo - Porcentagem encontrada
Pagamento final - Pagamento com acréscimo
```

## Diferencial
- Implementação ou integração de ferramenta para visualização do relatório final

## Envio do projeto / Dúvidas
- Arquivos
- Ferramentas
- Imagens

**Enviar para o email [dev@upbet.com](mailto:dev@upbet.com)**
