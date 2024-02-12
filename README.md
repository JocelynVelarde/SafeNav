
# SafeNav: Waze's Safety Upgrade 🚀

Do you often feel unsafe when going home? Want to know the most optimal safe route to get there?

Then, SafeNav is the answer for you! Just easily type or speak your desired initial point and final destination point, and we will provide you with the safest route to get there.

<img src="https://github.com/JocelynVelarde/SafeNav/assets/70779495/2f9e2f64-8409-40bc-8f4c-44c70a0bc079" alt="safenav profile" width="500" height="400">

## Authors

- [@JocelynVelarde](https://github.com/JocelynVelarde)
- [@Diego785xd](https://github.com/Diego785xd)



## Features

- Easily type or speak in natural language your desired route
- Translation from speech to text
- Implements LLMs to filter requests and provide route data
- Uses Dijkstra's algorithm for optimal pathfinding
- Takes into consideration criminal activity near each zone to provide a safe route
- Light and Dark mode enabled
- Available in all devices


## Structure
```bash
streamlit_app 
├─ home.py
├─ .streamlit
│   └─ secrets.toml
│   └─ gcloud.json
├─ algorithms
├─ api
├─ assets
│  └─ files
│  └─ images
├─ pages
│  └─ report_bug.py
│  └─ get_started.py
│  └─ route.py
└─ requirements.txt
```

## Tools

- OpenAI API
- Streamlit
- streamlit-mic-recorder
- Google Sheets API

Deployed with: Streamlit Cloud
## Documentation

[DevPost](https://devpost.com/software/test-z8sixj?ref_content=user-portfolio&ref_feature=in_progress)


## License

[MIT](https://choosealicense.com/licenses/mit/)


