import { serve } from "https://deno.land/std@0.59.0/http/server.ts";
import { request } from "https://deno.land/x/request/mod.ts";

const s = serve({ port: 8080 });

const api_key = "api-key";

const queries: string[] = ["bitcoin", "ethereum", "dogecoin", "cryptocurrency"];

for await (const req of s) {
  try {
    const sentiments:any = [];

    for (const element of queries) {
      const url = `https://newsapi.org/v2/everything?q=${element}&from=2024-01-23&sortBy=popularity&apiKey=${api_key}`;
      
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();

      for (let i = 0; i < data.articles.length; i++) {
        const article = data.articles[i];
        const text = article.content;

        try {
          const sentimentResponse = await request({
            url: 'https://api.api-ninjas.com/v1/sentiment?text=' + text,
            headers: {
              'X-Api-Key': 'api-key', 
            },
          });

          const sentimentData = JSON.parse(sentimentResponse);
          sentiments.push(sentimentData);
        } catch (error) {
          console.error('Sentiment Analysis Error:', error);
        }

        console.log(text);
      }
    }

    const responseBody = JSON.stringify({ sentiments });
    req.respond({ body: responseBody });
  } catch (error) {
    console.error(`Error: ${error}`);
    req.respond({ status: 500, body: "Internal Server Error" });
  }
}
