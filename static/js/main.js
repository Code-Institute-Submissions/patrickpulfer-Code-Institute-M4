// Initializing DatePicker
$('.datepicker').datepicker({
    format: 'dddd, dd mmm, yyyy',
    formatSubmit: 'yyyy/mm/dd'
})


// Get Stripe publishable key
fetch("/payment/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
        const stripe = Stripe(data.publicKey);
        document.querySelector("#submitBtn").addEventListener("click", () => {
            fetch("/payment/create-checkout-session/")
                .then((result) => { return result.json(); })
                .then((data) => {
                    return stripe.redirectToCheckout({ sessionId: data.sessionId })
                })
                .then((res) => {
                    console.log(res);
                });
        });
    });


$( document ).ready(function() {
    $('.login, .signup, .email_list, .password_change').find(':input,:radio,:checkbox').addClass('form-control');
});


