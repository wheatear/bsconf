$(function () {
    $("#upload").click(function () {
        // $("#imgWait").show();
        var formData = new FormData();
        formData.append("jsonFile", document.getElementById("jsonFile").files[0]);
        $.ajax({
            url: "uploadFile",
            type: "POST",
            data: formData,
            /**
             *必须false才会自动加上正确的Content-Type
             */
            contentType: false,
            /**
             * 必须false才会避开jQuery对 formdata 的默认处理
             * XMLHttpRequest会对 formdata 进行正确的处理
             */
            processData: false,
            success: function (data) {
                alert("upload success")
                // if (data.status == "true") {
                //     alert("上传成功！");
                // }
                // if (data.status == "error") {
                //     alert(data.msg);
                // }
                // $("#imgWait").hide();
            },
            error: function () {
                alert("上传失败！");
                // $("#imgWait").hide();
            }
        });
    });

    $('#makeSql').click(function(){
        jsonFile = $("#jsonFile");
        jsonName = getFileName(jsonFile.val());

        alert(jsonName);
        data = {'jsonName': jsonName};
        $.ajax({
            url: "makeBsSql",
            type: "GET",
            data: {"jsonName":jsonName},
        }).done(function(){
            alert("make sql "+jsonName)
        });
        // $.get("makeSql", {"jsonName":jsonName}, function(){
        //     alert("make sql "+jsonName)
        // })
    });

    function getFileName(o){
        var pos=o.lastIndexOf("\\");
        return o.substring(pos+1);
    }
});

