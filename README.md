# Monitoramento SDN com P4

Este repositório contém o código e a documentação relacionados ao projeto de monitoramento de redes definidas por software (SDN) usando a linguagem P4. O projeto é parte de um trabalho de conclusão de curso (TCC) que visa avaliar o desempenho de redes SDN através de diferentes técnicas de monitoramento.

## Objetivo

O objetivo principal deste projeto é avaliar duas formas distintas de monitoramento de redes SDN e comparar suas métricas de desempenho, como atraso (delay), perda de pacotes (loss) e throughput. O projeto também explora a complexidade e as vantagens de cada método.

## Explicação dos Diretórios e Arquivos Mais relevantes para as técnicas

### Explicação dos Diretórios e Arquivos

- **`exercises`**: Contém scripts e arquivos relacionados aos exercícios de monitoramento e topologia de rede. Inclui configurações, scripts de teste e imagens.

- **`LICENSE`**: Licença do projeto.

- **`p4-cheat-sheet.pdf`** e **`P4_tutorial.pdf`**: Documentos adicionais que fornecem informações sobre a linguagem P4.

- **`README.md`**: Documentação principal do projeto.

- **`utils`**: Contém utilitários e ferramentas auxiliares, incluindo scripts para Mininet e P4Runtime, bem como documentação e exemplos.

- **`vm`**: Arquivos relacionados à configuração da máquina virtual para o projeto.

- **`vm-ubuntu-20.04`**: Configurações e scripts para uma VM específica com Ubuntu 20.04, incluindo patches e scripts de bootstrap.

Esta estrutura organiza os arquivos de forma que você possa encontrar facilmente os scripts, configurações e documentação necessários para o projeto.


monitoramentoSDN-tcc/
├── exercises
│ ├── link_monitor
│ │ ├── executa_ida.sh # Script para executar testes de ida
│ │ ├── executa_volta.sh # Script para executar testes de volta
│ │ ├── link_monitor.p4 # Código P4 para monitoramento de links
│ │ ├── link-monitor-topo.png # Imagem da topologia de rede
│ │ ├── Makefile # Arquivo de build para o diretório link_monitor
│ │ ├── pod-topo
│ │ │ ├── s1-runtime.json # Configurações de runtime para o switch s1
│ │ │ ├── s2-runtime.json # Configurações de runtime para o switch s2
│ │ │ ├── s3-runtime.json # Configurações de runtime para o switch s3
│ │ │ ├── s4-runtime.json # Configurações de runtime para o switch s4
│ │ │ └── topology.json # Configuração da topologia de rede
│ │ ├── probe_hdrs.py # Script para cabeçalhos de probe
│ │ ├── README.md # Documentação para o diretório link_monitor
│ │ ├── receive.py # Script para receber pacotes
│ │ ├── rodar_ping.sh # Script para rodar ping
│ │ ├── send.py # Script para enviar pacotes
│ │ └── send_volta.py # Script para enviar pacotes na direção oposta
│ ├── ping
│ │ └── rodar_ping.sh # Script para rodar ping no diretório ping
│ └── topologia.png # Imagem da topologia de rede
├── LICENSE # Licença do projeto
├── p4-cheat-sheet.pdf # Folha de dicas sobre P4
├── P4_tutorial.pdf # Tutorial sobre a linguagem P4
├── README.md # Documentação principal do projeto
├── utils # pasta com utilidades
│ ├── Makefile # Arquivo de build para o diretório utils
│ ├── mininet
│ │ ├── appcontroller.py # Script para controle de aplicação no Mininet
│ │ ├── apptopo.py # Script para topologia de aplicação no Mininet
│ │ ├── multi_switch_mininet.py # Script para Mininet com múltiplos switches
│ │ ├── p4_mininet.py # Script para integração do P4 com Mininet
│ │ ├── shortest_path.py # Script para cálculo do caminho mais curto
│ │ └── single_switch_mininet.py # Script para Mininet com um único switch
│ ├── netstat.py # Script para monitorar estatísticas de rede
│ ├── p4apprunner.py # Script para execução de aplicações P4
│ ├── p4_mininet.py # Script para Mininet com suporte a P4
│ ├── p4runtime_lib
│ │ ├── bmv2.py # Biblioteca para BMv2
│ │ ├── convert.py # Script para conversão de dados
│ │ ├── error_utils.py # Utilitários para gerenciamento de erros
│ │ ├── helper.py # Funções auxiliares
│ │ ├── init.py # Inicializador da biblioteca
│ │ ├── simple_controller.py # Controlador simples para P4Runtime
│ │ └── switch.py # Script para configuração de switches
│ ├── p4runtime_switch.py # Script para interação com switches P4Runtime
│ └── run_exercise.py # Script para execução de exercícios
├── clean.sh # Script para limpeza do ambiente
├── p4_16-mode.el # Configuração do modo P4-16 para Emacs
├── p4-logo.png # Logo do P4
