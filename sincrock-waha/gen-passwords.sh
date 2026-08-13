#!/usr/bin/env bash

# Generate random secrets and admin user
sed -i.bak \
    -e "s#WAHA_API_KEY=.*#WAHA_API_KEY=$(openssl rand -hex 32)#g" \
    -e "s#WAHA_DASHBOARD_PASSWORD=admin!:.*#WAHA_DASHBOARD_PASSWORD=admin!:$(openssl rand -hex 16)#g" \
    -e "s#WHATSAPP_SWAGGER_PASSWORD=admin!:.*#WHATSAPP_SWAGGER_PASSWORD=admin!:$(openssl rand -hex 16)#g" \
    "$(dirname "$0")/.env"