jsonData = {};
$(function () {
    // $("#json").JSONView(json);
    // jsonData = {};

    $('#reqType').val(localStorage.reqType);
    $('#author').val(localStorage.author);
    $('#month').val(localStorage.month);
    $('#reqName').val(localStorage.reqName);
    var reqName = localStorage.reqName;
    jsonData[reqName] = {};

    // alert("open json of "+ reqName);
    openReqConf();


    function openReqConf () {
        var dReq = {
            "type":$('#reqType').val(),
            "month":$('#month').val(),
            "author":$('#author').val(),
            "reqName": $("#reqName").val()
        };
        if (dReq["reqName"] === ""){
            $("#json").html("");
            return
        }
        $.ajax({
            url: "/openReqConf/",
            type: "POST",
            data: dReq
        }).done(function (data) {
                // alert('open json file:');
                console.log(data);
                jsonData = data;
                // $.extend(true,jsonData,data);
                $("#json").JSONView(jsonData);
                refreshCheck(jsonData);
                // $('#downloadSql').href(path + "/" + sqlFile);
                // qryReqm();
        }).fail(function(){
            // alert("打开需求配置失败");
            refreshCheck({});
        });
    }

    function refreshCheck(jsonData){
        // alert("refresh check");
        $("[name='reqblock']").removeAttr("checked");
        // $.each($('input:checkbox:checked'),function(){
        //     $(this).prop("checked","false")
        // });
        var reqName = $("#reqName").val();
        console.log(reqName);
        console.log(jsonData);
        $.each(jsonData[reqName], function(k,v){
            // alert("block "+ k);
            var chk = "#blockSelecter #" + k;
            $(chk).prop("checked","true")
            // $('input:checkbox:'+k).prop("checked","true")
        })
    }

    $("#query").click(function(){
        $("#reqName").val("");
        localStorage.reqName = "";
        jsonData = {};
        $("#json").html("");
        $("[name='reqblock']").removeAttr("checked");
    });

    $("#selectBlock").click(function(){
        var reqName = $("#reqName").val();
        if ( ! reqName){
            alert("请输入解决方案名称");
            return;
        }
        localStorage.reqName = reqName;
        openReqConf();
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
        if (aBlock.length === 0){
            return
        }
        var dBlockName = {"blockName": aBlock};
        // alert("block name: " + aBlock);
        $.ajax({
            url: "/getDataTpl/",
            type: "POST",
            data: dBlockName
        }).done(function (data) {
                var reqName = $("#reqName").val();
                oldData = jsonData[reqName];
                $.extend(true, data, oldData);
                jsonData[reqName] = data;
                $("#json").JSONView(jsonData);
        }).fail(function(){
            alert("取数据模板失败")
        })
    });

    $("#makeSql").click(function(){
        jsonData = $('#json').JSONParse();
        var dReq = {
            "type":$('#reqType').val(),
            "month":$('#month').val(),
            "author":$('#author').val(),
            "reqName": $("#reqName").val(),
            "reqJson": JSON.stringify(jsonData)
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
            $("#downloadSql").attr({"href": ''});
            alert("生成配置SQL失败")
        })
    })
});
