document.addEventListener('DOMContentLoaded', function () {
  const languageCode = document.querySelector('#language_code');
  const translateButton = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  translateButton.addEventListener('click', function () {
    const language = languageCode.value;

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${language}`)
      .then(response => response.json())
      .then(data => {
        hello.textContent = data.hello;
      });
  });
});
