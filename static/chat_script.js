
async function SendMsg() {
    $.ajax({
            type: "POST",
            url: "/send_msg",
            dataType: "json",
            data: JSON.stringify({
                "chat_id": document.getElementById('IDholder').innerHTML,
                "user_message": $('textarea#message').val()
            })
    });
}