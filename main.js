setInterval(function() {

	widget.system("./get_harvest_tasks.py ian@thirdmind.com ith383lt1 | ./get_task_notes.py | ./set_skype_mood.py", function(obj) {

	});

}, 30000);