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

    $("#selectBlock").click(function(){
        if ( ! $("#reqDoc").val()){
            alert("请输入解决方案名称");
            return;
        }
        $selectPop = $("#blockSelecter");
        $selectPop.show()
    });

    $("#shutoff").click(function(){
        var $selectPop = $("#blockSelecter");
        $selectPop.hide();
        var aBlock = [];
        $.each($('input:checkbox:checked'),function(){
            aBlock.push($(this).val())
        });
        var dBlockName = {"blockName": aBlock};
        // alert("block name: " + aBlock);
        $.ajax({
            url: "/getDataTpl/",
            type: "POST",
            data: dBlockName
        }).done(function (data) {
                var reqName = $("#reqDoc").val();
                var jsonTpl = {};
                jsonTpl[reqName] = data;
                $("#json").JSONView(jsonTpl);
        }).fail(function(){
            alert("取数据模板失败")
        })
    });

    $("#makeSql").click(function(){
        var reqJson = $('#json').JSONParse();
        var dReq = {
            "type":$('#reqType').val(),
            "month":$('#month').val(),
            "author":$('#author').val(),
            "reqName": $("#reqDoc").val(),
            "reqJson": JSON.stringify(reqJson)
        };
        // dReq["reqJson"] = reqJson;
        // $.extend(true,dReq,reqJson);
        // alert(JSON.stringify(dReq));
        $.ajax({
            url: "/makeSql/",
            type: "POST",
            data: dReq
        }).done(function (data) {
            var sqlFile = data.sqlFile;
            var path = data.downPath;
            var errCode = data.errCode;
            var errDesc = data.errDesc;
            $("#downloadSql").attr({"href": '/' + path + '/' + sqlFile});
            alert("sql file: " + sqlFile + "\nresult: " + errCode + " ( " + errDesc +" )");
            if (parseInt(errCode) < 7) {
                $("#downloadSql").hide()
            } else {
                $("#downloadSql").show()
            }

        }).fail(function(){
            alert("取数据模板失败")
        })
    })
});
