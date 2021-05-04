/*
 * Modals closed event
 */
$('#loginModal').on('hidden.bs.modal', () => {
  document.getElementById('login-form').reset();
});

$('#registerModal').on('hidden.bs.modal', () => {
  document.getElementById('register-form').reset();
});