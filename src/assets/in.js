
import EmbedSDK from '@mongodb-js/charts-embed-dom';

const sdk= new EmbedSDK({
    baseUrl: 'https://charts.mongodb.com/charts-project-0-uswvr'
  });

const chart1 = sdk.createChart({chartId: 'd0299ac3-51ae-41ae-920a-b427514b0d04'});

chart1.render(document.getElementById("chart1"));
