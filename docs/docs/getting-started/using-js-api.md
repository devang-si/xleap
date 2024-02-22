---
sidebar_position: 1
---

# Typescript/Javascript
Here's how to integrate: 
1. Navigate to account settings and generate an API Key for CLI. 
2. Copy the API key, as it will be needed for the next step.
3. Begin sending the data through one of the available methods.

## Setup using typescript/javascript

```tsx title="setup.ts"
const BASE_URL = 'https://api.xleaplabs.com';
const API_KEY = '<********* private key from dashboard>'; // should be private

const response = await fetch(`${BASE_URL}/v1/api/data`, {
  method: 'POST',
  headers: {
    'Authorization': `API_KEY ${API_KEY}`,
    'content-type': 'application/json',
  },
  body: JSON.stringify({
    question: '<Your question or prompt template with {context_var}>',
    answer: '<llm response as text or stringified json>',
    contexts: ['<array of strings sent to the llm model as key value pair>', 'context_var: this is sample context'],
    ground_truths: [],
    tags: { key: 'value' },
  }),
});

console.log(response);
```
