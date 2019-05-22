$(function () {
    var dReq = {
        "type":"ZG"
    };
    aRequirement = null;
    $reqTab = $('#con');
    $activeReq = null;

    // // fill month
    // (function(){
    //     $hMonth = $("#month");
    //     tNow = new Date();
    //     $hMonth.empty();
    //     strNow = getYYYYMM(tNow);
    //     $hMonth.append("<option selected=\"selected\" value=\"" + strNow + "\">" + strNow + "</option>");
    //     for(var i=1;i<12;i++){
    //
    //     }
    // })();
    $('#reqType').val(localStorage.reqType);
    $('#author').val(localStorage.author);

    function getYYYYMM(date){
        yyyy =date.getFullYear();
        month = date.getMonth()+1;
        strMon = month > 9 ? month : '0'+month;
        return yyyy + "" + strMon
    }

    function qryReqm(){
        dReq = {
            "type":$('#reqType').val(),
            "month":$('#month').val(),
            "author":$('#author').val()
        };
        // alert("type: " + dReq.type + " month: " + dReq.month);
        $.ajax({url:"qryRequirement",type: "GET",
            data:dReq
        }).done(function(aReqm){
            aRequirement = aReqm;
            aRequirement.sortId = 'json';
            // var hTab = $('#con');
            fillTable(aReqm.bsReq,$reqTab)
        }).fail(function(rep){
            alert("qryRequirement fail: " + rep);
            errMsg = "";
            $.each(rep, function(i,d){
                errMsg = errMsg + i + " | " + d + "\n"
            });
            alert(errMsg)
        });
    }

    qryReqm();

    $("#query").click(function(){
        qryReqm();
    });

    $("#uploadMmakeSql").click(function () {
        // $("#imgWait").show();
        var formData = new FormData();
        formData.append("jsonFile", document.getElementById("jsonFile").files[0]);
        // var dReq = {
        //     "type":$('#reqType').val()
        // };
        formData.append("type", $('#reqType').val());
        formData.append("author", $('#author').val());
        $.ajax({
            url: "uploadMakeSql",
            type: "POST",
            data: formData,
             // *必须false才会自动加上正确的Content-Type
            contentType: false,

             // * 必须false才会避开jQuery对 formdata 的默认处理
             // * XMLHttpRequest会对 formdata 进行正确的处理
            processData: false,
            success: function (data) {
                var sqlFile = data.sqlFile;
                var path = data.downPath;
                var errCode = data.errCode;
                var errDesc = data.errDesc;
                // alert("sqlfile: " + sqlFile + path);
                $("#downloadSql").attr({"href": path + '/' + sqlFile});
                alert("sql file: " + sqlFile + "\nresult: " + errCode + " ( " + errDesc +" )");
                if (parseInt(errCode) < 7) {
                    $("#downloadSql").hide()
                } else {
                    $("#downloadSql").show()
                }
                // $('#downloadSql').href(path + "/" + sqlFile);
                qryReqm();
            },
            error: function () {
                alert("生成SQL文件失败！");
                // $("#imgWait").hide();
            }
        });
    });

    // $reqList = $('#con');
    $('#reqType').change(function(ev){
        localStorage.reqType = $(this).val();
    });

    $('#author').change(function(ev){
        localStorage.author = $(this).val();
    });


    $reqTab.delegate('.bodyCon', 'click', function(event) {
        if ($activeReq) {
            $activeReq.removeClass('active');
        }

        $(this).addClass('active');
        $activeReq = $(this);
    });

    $reqTab.delegate('th', 'click', function(event){
        // alert($(this).attr('id'));
        aRequirement.sortId = $(this).attr('id');
        var newReq = aRequirement.bsReq.sort(sortReq);
        // alert(aRequirement.sortId);
        // $.each(newReq,function(i,v){
        //     alert(v['json_file'])
        // });

        fillTable(newReq,$reqTab)
    });

    function sortReq(a,b){
        if (a[aRequirement.sortId] < b[aRequirement.sortId]) {return -1}
        else if (a[aRequirement.sortId] > b[aRequirement.sortId]) {return 1}
        else {return 0}

    }
    // $("#con tr").click(function(){
    //
    // });

    $("#saveJson").click(function(){
        var formData = new FormData();
        formData.append("jsonFile", document.getElementById("jsonFile").files[0]);
        $.ajax({
            url: "saveJson",
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
                var path = data.sqlFile;
                // $("#sqlFile").href = path;
                alert("上传json文件: " + getFileName($("#jsonFile").val()) + " success")
                // if (data.status == "true") {
                //     alert("上传成功！");
                // }
                // if (data.status == "error") {
                //     alert(data.msg);
                // }
                // $("#imgWait").hide();
                qryReqm();
            },
            error: function () {
                alert("上传失败！");
                // $("#imgWait").hide();
            }
        });
    });

    $('#makeSql0').click(function(){
        jsonFile = $("#jsonFile");
        jsonName = getFileName(jsonFile.val());

        alert(jsonName);
        data = {'jsonName': jsonName};
        $.ajax({
            url: "makeBsSql",
            type: "GET",
            data: {"jsonName":jsonName}
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

    //fill select
    function fillTable(aReqm,hTab){
        hTab.empty();
        tabHead = "<tr class=\"bodyHead\">" +
            "        <th class=\"json\" id=\"json_file\">json文件</th>" +
            "        <th class=\"state\" id=\"state\">状态</th>" +
            "        <th class=\"month\" id=\"req_month\">月份</th>" +
            "        <th class=\"sql\" id=\"sql_file\">sql文件</th>" +
            "        <th class=\"type\" id=\"conf_type\">模块</th>" +
            "        <th class=\"createtime\" id=\"create_date\">生成时间</th>" +
            "        <th class=\"updatetime\" id=\"update_date\">更改时间</th>" +
            "    </tr>";
        hTab.append(tabHead);
        $.each(aReqm, function(i,dName){
            // alert(i + dName)
            json = dName["json_file"];

            trReqm = "<tr class=\"bodyCon\">" +
                "        <td class=\"json\" id=\"json\">" + dName["json_file"] + "</td>" +
                "        <td class=\"state\" id=\"state\">" + dName["state"] + "</td>" +
                "        <td class=\"month\" id=\"month\">" + dName["req_month"] + "</td>" +
                "        <td class=\"sql\" id=\"sql\">" + dName["sql_file"] + "</td>" +
                "        <td class=\"type\" id=\"type\">" + dName["conf_type"] + "</td>" +
                "        <td class=\"createtime\" id=\"createtime\">" + dName["create_date"] + "</td>" +
                "        <td class=\"updatetime\" id=\"updatetime\">" + dName["update_date"] + "</td>" +
                "    </tr>";
            // alert(trReqm);
            hTab.append(trReqm);
        });

    }
});

