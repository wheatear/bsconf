$(function () {
    // $("#json").JSONView(json);

    $("#openJson").click(function () {
        var formData = new FormData();
        formData.append("jsonFile", document.getElementById("jsonFile").files[0]);
        // var dReq = {
        //     "type":$('#reqType').val()
        // };
        // formData.append("type", $('#reqType').val());
        // formData.append("author", $('#author').val());
        $.ajax({
            url: "openJson",
            type: "POST",
            data: formData,
             // *必须false才会自动加上正确的Content-Type
            contentType: false,
             // * 必须false才会避开jQuery对 formdata 的默认处理
             // * XMLHttpRequest会对 formdata 进行正确的处理
            processData: false,
            success: function (data) {
                alert('open json file:');
                alert(data);
                $("#json").JSONView(data);
                // $('#downloadSql').href(path + "/" + sqlFile);
                // qryReqm();
            },
            error: function () {
                alert("生成SQL文件失败！");
                // $("#imgWait").hide();
            }
        });
    });

});
