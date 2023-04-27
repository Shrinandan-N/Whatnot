document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;
    const message = document.querySelector('#message').value;
    const csrfToken = document.querySelector('[name="csrf_token"]').value;
    const fileInput = document.querySelector('#file');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('message', message);
    formData.append('file', file);
    const response = await fetch('/start', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken
      },
      body: formData
    });
    const result = await response.json();
    console.log(result);
  });
});
