#!/bin/bash

# Loop para executar o comando ping 30 vezes
for i in {1..30}
do
    # Executa o comando ping e filtra as linhas que começam com "rtt" ou contêm "---"
    ping -c 50 10.0.3.3 | grep -E '^(rtt|50)' >> ping_output.txt
done
