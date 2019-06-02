(function(jQuery) {
  var $, Collapser, JSONFormatter, JSONView;
  JSONFormatter = (function() {
    function JSONFormatter(options) {
      if (options == null) {
        options = {};
      }
      this.options = options;
    }

    JSONFormatter.prototype.htmlEncode = function(html) {
      if (html !== null) {
        return html.toString().replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
      } else {
        return '';
      }
    };

    JSONFormatter.prototype.jsString = function(s) {
      s = JSON.stringify(s).slice(1, -1);
      return this.htmlEncode(s);
    };

    JSONFormatter.prototype.decorateWithSpan = function(value, className) {
      return "<span class=\"" + className + "\"><input type='text' value=\"" + (this.htmlEncode(value)) + "\" /></span>";
    };

    JSONFormatter.prototype.valueToHTML = function(value, level) {
      var valueType;
      if (level == null) {
        level = 0;
      }
      valueType = Object.prototype.toString.call(value).match(/\s(.+)]/)[1].toLowerCase();
      return this["" + valueType + "ToHTML"].call(this, value, level);
    };

    JSONFormatter.prototype.nullToHTML = function(value) {
      return this.decorateWithSpan('null', 'null');
    };

    JSONFormatter.prototype.numberToHTML = function(value) {
      return this.decorateWithSpan(value, 'num');
    };

    JSONFormatter.prototype.stringToHTML = function(value) {
      var multilineClass, newLinePattern;
      if (/^(http|https|file):\/\/[^\s]+$/i.test(value)) {
        return "<a href=\"" + (this.htmlEncode(value)) + "\"><span class=\"q\">\"</span>" + (this.jsString(value)) + "<span class=\"q\">\"</span></a>";
      } else {
        multilineClass = '';
        value = this.jsString(value);
        if (this.options.nl2br) {
          newLinePattern = /([^>\\r\\n]?)(\\r\\n|\\n\\r|\\r|\\n)/g;
          if (newLinePattern.test(value)) {
            multilineClass = ' multiline';
            value = (value + '').replace(newLinePattern, '$1' + '<br />');
          }
        }
        return "<span class=\"string" + multilineClass + "\"><input type='text' value=\"" + value + "\" /></span>";
      }
    };

    JSONFormatter.prototype.booleanToHTML = function(value) {
      return this.decorateWithSpan(value, 'bool');
    };

    JSONFormatter.prototype.arrayToHTML = function(array, level) {
      var collapsible, hasContents, index, numProps, output, value, _i, _len;
      if (level == null) {
        level = 0;
      }
      hasContents = false;
      output = '';
      numProps = array.length;
      for (index = _i = 0, _len = array.length; _i < _len; index = ++_i) {
        value = array[index];
        hasContents = true;
        output += '<li>' + this.valueToHTML(value, level + 1);
        // if (numProps > 1) {
        //   output += ',';
        // }
        var valueType = Object.prototype.toString.call(value).match(/\s(.+)]/)[1].toLowerCase();
        switch (valueType){
            case 'array':
              break;
            case 'object':
              break;
            default:
              output += '<span class=\'btn\'><button type=\'button\' class=\'editbtn\'>d</button></span></li>';
        }
        numProps--;
      }
      if (hasContents) {
        collapsible = level === 0 ? '' : ' collapsible';
        return "<span class='btn'><button type='button' class='editbtn'>a</button><button type='button' class='editbtn'>d</button></span><ul class=\"array level" + level + collapsible + "\">" + output + "</ul>";
      } else {
        return '[ ]';
      }
    };

    JSONFormatter.prototype.objectToHTML = function(object, level) {
      var collapsible, hasContents, numProps, output, prop, value;
      if (level == null) {
        level = 0;
      }
      hasContents = false;
      output = '';
      numProps = 0;
      for (prop in object) {
        numProps++;
      }
      for (prop in object) {
        value = object[prop];
        hasContents = true;
        output += "<li><span class=\"prop\"> " + (this.jsString(prop)) + "</span>: " + (this.valueToHTML(value, level + 1));
        // if (numProps > 1) {
        //   output += ',';
        // }
        var valueType = Object.prototype.toString.call(value).match(/\s(.+)]/)[1].toLowerCase();
        switch (valueType){
            case 'array':
              break;
            case 'object':
              break;
            default:
              output += '<span class=\'btn\'><button type=\'button\' class=\'editbtn\'>d</button></span></li>';
        }
        numProps--;
      }
      if (hasContents) {
        collapsible = level === 0 ? '' : ' collapsible';
        return "<span class='btn'><button type='button' class='editbtn'>d</button></span><ul class=\"obj level" + level + collapsible + "\">" + output + "</ul>";
      } else {
        return '<span class=\'btn\'><button type=\'button\' class=\'editbtn\'>d</button></span>{ }';
      }
    };

    JSONFormatter.prototype.jsonToHTML = function(json) {
      return "<div class=\"jsonview\">" + (this.valueToHTML(json)) + "</div>";
    };

    return JSONFormatter;

  })();
  (typeof module !== "undefined" && module !== null) && (module.exports = JSONFormatter);
  Collapser = {
    bindEvent: function(item, collapsed) {
      var collapser;
      collapser = document.createElement('div');
      collapser.className = 'collapser';
      collapser.innerHTML = collapsed ? '+' : '-';
      collapser.addEventListener('click', (function(_this) {
        return function(event) {
          return _this.toggle(event.target);
        };
      })(this));
      item.insertBefore(collapser, item.firstChild);
      if (collapsed) {
        return this.collapse(collapser);
      }
    },
    expand: function(collapser) {
      var ellipsis, target;
      target = this.collapseTarget(collapser);
      ellipsis = target.parentNode.getElementsByClassName('ellipsis')[0];
      target.parentNode.removeChild(ellipsis);
      target.style.display = '';
      return collapser.innerHTML = '-';
    },
    collapse: function(collapser) {
      var ellipsis, target;
      target = this.collapseTarget(collapser);
      target.style.display = 'none';
      ellipsis = document.createElement('span');
      ellipsis.className = 'ellipsis';
      ellipsis.innerHTML = ' &hellip; ';
      target.parentNode.insertBefore(ellipsis, target);
      return collapser.innerHTML = '+';
    },
    toggle: function(collapser) {
      var target;
      target = this.collapseTarget(collapser);
      if (target.style.display === 'none') {
        return this.expand(collapser);
      } else {
        return this.collapse(collapser);
      }
    },
    collapseTarget: function(collapser) {
      var target, targets;
      targets = collapser.parentNode.getElementsByClassName('collapsible');
      if (!targets.length) {
        return;
      }
      return target = targets[0];
    }
  };
  $ = jQuery;
  JSONParser = {
    parseNumber: function (el) {
      return el.children('input')[0].value
    },
    parseString: function(el) {
      return el.children('input')[0].value
    },
    parseObj: function (el) {
      var obj = {};
      el.children('li').each(function(){
        var prName = $(this).children('.prop').text().substr(1);
        obj[prName] = JSONParser.parseVal($(this));
      });
      return obj;
    },
    parseArr: function (el) {
      var arr = [];
      el.children('li').each(function(){
        arr.push(JSONParser.parseVal($(this)))
      });
      return arr;
    },
    parseVal: function(el){
      var propVal;
      if (el.children().hasClass('obj')){
        propVal = JSONParser.parseObj(el.children('.obj'))
      } else if(el.children().hasClass('array')){
        propVal = JSONParser.parseArr(el.children('.array'))
      } else if(el.children().hasClass('string')){
        propVal = JSONParser.parseString(el.children('.string'))
      } else if(el.children().hasClass('num')){
        propVal = JSONParser.parseNumber(el.children('.num'))
      } else if(el.text().indexOf('{ }')>0){
        console.log(el.text());
        propVal = {}
      }
      // if(el.innerHTML.indexof('{ }')>0)
      return propVal;
    },
    parseJsonView: function(el){
      var json = {};
      var $this = $(this);
      el.find(".jsonview").children('ul.obj.level0').each(function(){
        $(this).children('li').each(function(){
          var prName = $(this).children('.prop').text().substr(1);
          var propVal = JSONParser.parseVal($(this));
          json[prName] = propVal
          // $.extend(json,{prName: propVal})
        })
      });
      return json;
    }
  };
  $.fn.JSONParse = function() {
    var jsonData, $this;
    $this = $(this);
    jsonData = JSONParser.parseJsonView($this);
    console.log(jsonData);
    // alert(JSON.stringify(jsonData));
    return jsonData;

  };
  JSONView = {
    collapse: function(el) {
      if (el.innerHTML === '-') {
        return Collapser.collapse(el);
      }
    },
    expand: function(el) {
      if (el.innerHTML === '+') {
        return Collapser.expand(el);
      }
    },
    toggle: function(el) {
      return Collapser.toggle(el);
    }
  };
  return $.fn.JSONView = function() {
    var args, defaultOptions, formatter, json, method, options, outputDoc;
    args = arguments;
    if (JSONView[args[0]] != null) {
      method = args[0];
      return this.each(function() {
        var $this, level;
        $this = $(this);
        if (args[1] != null) {
          level = args[1];
          return $this.find(".jsonview .collapsible.level" + level).siblings('.collapser').each(function() {
            return JSONView[method](this);
          });
        } else {
          return $this.find('.jsonview > ul > li > .collapsible').siblings('.collapser').each(function() {
            return JSONView[method](this);
          });
        }
      });
    } else {
      json = args[0];
      options = args[1] || {};
      defaultOptions = {
        collapsed: false,
        nl2br: false
      };
      options = $.extend(defaultOptions, options);
      formatter = new JSONFormatter({
        nl2br: options.nl2br
      });
      if (Object.prototype.toString.call(json) === '[object String]') {
        json = JSON.parse(json);
      }
      outputDoc = formatter.jsonToHTML(json);
      return this.each(function() {
        var $this, item, items, _i, _len, _results;
        $this = $(this);
        $this.html(outputDoc);
        $this.delegate('button', 'click', function(ev){
            switch($(this).text()){
                case 'd':
                    ev.target.parentNode.parentNode.remove();
                    break;
                case 'a':
                    pn = ev.target.parentNode.parentNode.getElementsByClassName('collapsible')[0];
                    cn = pn.getElementsByTagName('li')[0];
                    $cn = $(cn);
                    $(pn).append($cn.clone(true,true));
                    break;
            }
        });
        items = $this[0].getElementsByClassName('collapsible');
        _results = [];
        for (_i = 0, _len = items.length; _i < _len; _i++) {
          item = items[_i];
          if (item.parentNode.nodeName === 'LI') {
            _results.push(Collapser.bindEvent(item.parentNode, options.collapsed));
          } else {
            _results.push(void 0);
          }
        }
        return _results;
      });
    }
  };
})(jQuery);
