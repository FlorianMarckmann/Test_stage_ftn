$(document).ready(function() {
	$.getJSON('./API/data_issues.json', function(jd) {
	   var i = 0;
	   while (jd.issue[i])
	   {
		   i++;
	   }
	   var html = '';
	   html += '<div class="row panel">';
	   html += '<p>'+ i +' '+ 'Open</p>';
	   html += '</div>';
	   $.each(jd.issue, function(key, value){
		  html += '<div class="row panel">';
		  html += '<div class="col">';
		  html += '<svg class="octicon octicon-issue-opened open" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"></path></svg>'
		  html += '<a>'+value.title+'</a>';
		  html += '<p class="font-italic text-justify">#'+value.number+'</p>';
		  html += '</div>';
		  html += '</div>';
	  });
	  $('#data_container').html(html);
	});
 });