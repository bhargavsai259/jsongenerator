pip install fastapi uvicorn groq python-dotenv


These packages are for:

fastapi → backend framework

uvicorn → server

groq → Groq LLM API

python-dotenv → to load API key safely


https://console.groq.com/docs/libraries  read this for groq documentation


Temperature Range
Temperature	Meaning
0.0	Fully deterministic (no randomness)
0.1 – 0.3	Very low randomness (best for coding, JSON, math)
0.4 – 0.7	Balanced (normal use cases)
0.8 – 1.0	Creative, more diverse
1.1 – 2.0	Highly creative, unpredictable (rarely needed)



Top-P Range
Top-P	Meaning
0.1 – 0.3	Very narrow selection → highly focused output
0.4 – 0.7	Balanced sampling
0.8 – 1.0	More creative, allows wide range of possible words