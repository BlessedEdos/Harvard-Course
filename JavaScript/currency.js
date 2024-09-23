document.addEventListener('DOMContentLoaded', function () {

  document.querySelector('form').onsubmit = function () {

      // Define the API key
    const apiKey = 'f8f28822e1-0d16da5665-sk9iz7';

    fetch(`https://api.fastforex.io/fetch-all?api_key=${apiKey}`)
    .then(response => response.json())
    .then(data => {
      const currency = document.querySelector('#currency').value.toUpperCase();
      const rate = data.results[currency];

      if (rate !== undefined) {
        document.querySelector('#output').innerHTML = ` 1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
      } else {
        document.querySelector('#output').innerHTML = `Sorry, we don't support ${currency}.`;
      }
    })

    .catch(error => {
      console.error('Error:', error);
    })

    return false;

  }

})