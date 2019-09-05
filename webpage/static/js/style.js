
$(function(){
	
	//流程配置布局
	$('.box_lcpz_img').height(document.documentElement.clientHeight - 315);
	//菜单
	$('.header_user .btn_tr').click(function() {
		$(this).parent().toggleClass('hav');
	});
	$('.menu_left li').click(function() {
		$('.menu_left li').removeClass('on');
		$(this).addClass('on')
	});
	
	
	/*菜单树*/
	$('.tree_box').siblings('.box_content').addClass('hav_tree');
	$('.tree_box').height($('.box_content').height());
	$('.tree_box .btn_l_r').click(function(){
		$(this).parent().parent().parent().parent().toggleClass('tree_hide')
	})
	//菜单图标
	$('.page_r_m .panel:eq(1) .panel-header').css('backgroundImage','url(css/images/menu_a_lcgl.png)');
	$('.page_r_m .panel:eq(2) .panel-header').css('backgroundImage','url(css/images/menu_a_ywgl.png)');
	$('.page_r_m .panel:eq(3) .panel-header').css('backgroundImage','url(css/images/menu_a_zsgl.png)');
	$('.page_r_m .panel:eq(4) .panel-header').css('backgroundImage','url(css/images/menu_a_wxgl.png)');
	$('.page_r_m .panel:eq(5) .panel-header').css('backgroundImage','url(css/images/menu_a_xxzx.png)');
	
	/*弹窗*/
	$('.btn_win_close').click(function() {
        $(".window").css("display","none");  
        $(".window-shadow").css("display","none");
	});
	$('.tc_hide_a').click(function(){
		$('.tc_text#tc_hide_a').removeClass('none')
		setTimeout(function () {  
        	$(".tc_text#tc_hide_a").addClass('none')
    	}, 1500); 
	})
	
	/*步骤*/
	$('.buzhou_a_next').click(function() {
        $('.buzhou_a').addClass('none').siblings('.buzhou_b').removeClass('none'); 
	});
	$('.buzhou_b_pre').click(function() {
        $('.buzhou_b').addClass('none').siblings('.buzhou_a').removeClass('none'); 
	});
	$('.cho_tubiao').click(function() {
        $('.cho_tubiao_hav').removeClass('none'); 
	});
	
	/*表格*/
	
	$('.tableStyleA .btn_org2').parent().addClass('p_ss');
	
	$('.cho_jg_a').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_a').removeClass('none'); 
	});
	$('.cho_jg_b').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_b').removeClass('none'); 
	});
	$('.cho_jg_c').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_c').removeClass('none'); 
	});
	$('.cho_jg_d').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_d').removeClass('none'); 
	});
	$('.cho_jg_e').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_e').removeClass('none'); 
	});
	$('.cho_jg_f').click(function() {
        $('.box_jg').addClass('none'); 
        $('.box_jg_f').removeClass('none'); 
	});
	 
/*勾选表格行 全选全不选*/
	$('.hav_qx input:checked').removeAttr('checked');
	$('.hav_qx td input:checkbox').click(function(){
		$(this).parent().parent().toggleClass('tr_chose')
		$('.hav_qx th input:checkbox').removeAttr('checked');
	});
	$('.hav_qx th input:checkbox').click(function(){   
        if(this.checked){  
			$(this).parent().parent().siblings().find('td :checkbox').parent().parent().addClass('tr_chose')
            $(this).parent().parent().siblings().find('td input:checkbox').attr('checked', true);  
        }else{   
			$('.hav_qx td :checkbox').parent().parent().removeClass('tr_chose')
            $('.hav_qx td :checkbox').attr('checked', false);
        }   
     })
	 
	
	/*全选全不选通用*/
	$('input.hav_check:checked').removeAttr('checked');
	$('input.hav_check:checkbox').click(function(){
		$(this).parent().siblings().find(':checkbox').removeAttr('checked');
	});
	$('input.hav_check:checkbox').click(function(){   
        if(this.checked){  
            $(this).parent().siblings().find(':checkbox').prop('checked', true);  
        }else{   
            $(this).parent().siblings().find(':checkbox').prop('checked', false);
        }   
     });  
	
	
	
	
	//tabs
	$('.tabs_tit li').click(function () {
        $(this).addClass('on').siblings().removeClass('on');

        var arr = $(this).parent().find('li');
        var idx = 0;
        for (var i = 0; i < arr.length; i++) {
            if ($(arr[i]).hasClass('on')) {
                idx = i;
                break;
            }
        }
        $(this).parent().siblings('.tabs_con').children('div').addClass('none');
        $(this).parent().siblings('.tabs_con').children('div').eq(idx).removeClass('none');
    });
	



})