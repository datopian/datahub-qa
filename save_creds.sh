#!/usr/bin/env bash

echo "Exporting datahub user credentials.";
echo "Don't worry, it is secured in the Travis!";

mkdir .config/datahub -p
cat <<EOF > ~/.config/datahub/config.json
{
  "token": "${DATAHUB_TOKEN}",
  "profile": {
    "avatar_url": "https://avatars0.githubusercontent.com/u/11707682?v=4",
    "email": "mryakzp@gmail.com",
    "id": "a08d3588fbae0355042537595c65819d",
    "join_date": "Thu, 07 Dec 2017 09:12:52 GMT",
    "name": "Dima German",
    "provider_id": "github:11707682",
    "username": "AcckiyGerman"
  }
}
EOF

cat ~/.config/datahub/config.json
