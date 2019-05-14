$(function () {
    dReq = {
        "type":"ZG"
    };
    function qryReqm(){
        dReq = {
            "type":$('#reqType').val()
        };
        alert(dReq.type);
        $.ajax({url:"qryRequirement",type: "GET",
            data:dReq
        }).done(function(aReqm){
            hTab = $('#con');
            fillTable(aReqm,hTab)
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
                var path = data.sqlFile;
                // $("#sqlFile").href = path;
                alert("生成SQL文件: " + path + " success")
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

    //fill select
    function fillTable(aReqm,hTab){
        hTab.empty();
        tabHead = "<tr>" +
            "        <th class=\"json\">json文件</th>" +
            "        <th class=\"state\">状态</th>" +
            "        <th class=\"month\">月份</th>" +
            "        <th class=\"sql\">sql文件</th>" +
            "        <th class=\"type\">模块</th>" +
            "        <th class=\"createtime\">生成时间</th>" +
            "        <th class=\"updatetime\">更改时间</th>" +
            "    </tr>";
        hTab.append(tabHead);
        $.each(aReqm.bsReq, function(i,dName){
            // alert(i + dName)
            json = dName["json_file"];

            trReqm = "<tr>" +
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

