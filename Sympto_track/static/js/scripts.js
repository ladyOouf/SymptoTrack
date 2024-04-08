// <!--Name of Code artifact: script.js
// Description: javascript of the code
// Authors: Sarah M
// Date Creation : November 17, 2023
// Date Revised: April 7th, 2024
// Preconditions: Empty Strings are not allowed.
// Postconditions: No return values.

$("form[name=signup_form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function () {
            window.location.href = "/";
        },
        error: function (resp) {
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});

$("form[name=login_form]").submit(function (e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/homepage/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

    e.preventDefault();
});

$("form[name=symptom_input]").submit(function (e) {
    e.preventDefault();

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/log_pain",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            console.log("Pain data logged successfully");
            window.location.href = "/homepage/";

        },
        error: function (resp) {
            console.error("Error logging pain data:", resp);
        }
    });
});


$("form[name=journal_input]").submit(function (e) {
    e.preventDefault();

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/journal_log",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            console.log("journal data logged successfully");
            window.location.href = "/homepage/";

        },
        error: function (resp) {
            console.error("Error logging journal data:", resp);
        }
    });
});
