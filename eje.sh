#!/bin/bash
# Copiar el contenido inicial de dns_queries.csv a dns_queries_graficador.csv
cp dns_queries.csv dns_queries_graficador.csv

# Inicializar el archivo dns_queries.csv con encabezado
echo "timestamp,queries_per_second" > dns_queries.csv

while true; do
    timestamp=$(date +%Y-%m-%dT%H:%M:%S)
    response=$(curl -sk -u 'admin:Qazplm123.' -H 'Content-Type: application/json' -X POST \
        -d '{"command": "run", "utilCmdArgs": "-c \"for i in {1..2}; do tmsh show /ltm profile dns dns_pruebas raw | grep '\''Total Queries'\'' | awk '\''{printf \\\"%sE\\\", $3}'\''; sleep 5; done | sed '\''s/E/ /g'\'' | awk '\''{print ($2-$1)/5}'\''\""}' \
        https://192.168.0.174/mgmt/tm/util/bash)

    echo "Response: $response"  # Imprime la respuesta para depuración
    
    qps=$(echo "$response" | jq -r .commandResult)
    echo "$timestamp,$qps" >> dns_queries.csv
    sleep 10  # Captura cada 10 minutos
done


