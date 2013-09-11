var HarvestMood = (function() {

	var data = {
		user: "",
		password: "",
		lunch_msg: "",
		idle_msg: ""
	}

	function _heartbeat() {
		if (data.user.length > 0 && data.password.length > 0)
			widget.system("./harvest_mood.py -u " + data.user + " -p " + data.password + " -l '" + data.lunch_msg + "' -i '" + data.idle_msg + "'", function(obj) {});
	}

	function _set_data(key, value) {
		if (key in data) {
			data[key] = value;
			widget.setPreferenceForKey(value, key);
		}
	}

	function _get_data(key) {
		if (key in data)
			return data[key];
	}

	function _get_data_preferences() {
		for(key in data) {
			data[key] = widget.preferenceForKey(key);
		}
	}

	return {
		init: function() {
			_get_data_preferences();

			setInterval(function() {
				_heartbeat();
			}, 5000);

			document.forms["HarvestMood"].elements["user"].value = HarvestMood.get_data("user");
			document.forms["HarvestMood"].elements["password"].value = HarvestMood.get_data("password");
			document.forms["HarvestMood"].elements["lunch_msg"].value = HarvestMood.get_data("lunch_msg");
			document.forms["HarvestMood"].elements["idle_msg"].value = HarvestMood.get_data("idle_msg");

			document.forms["HarvestMood"].elements["user"].addEventListener("keyup", function(e) {
				HarvestMood.set_data("user", this.value);
			});

			document.forms["HarvestMood"].elements["password"].addEventListener("keyup", function(e) {
				HarvestMood.set_data("password", this.value);
			});

			document.forms["HarvestMood"].elements["lunch_msg"].addEventListener("keyup", function(e) {
				HarvestMood.set_data("lunch_msg", this.value);
			});

			document.forms["HarvestMood"].elements["idle_msg"].addEventListener("keyup", function(e) {
				HarvestMood.set_data("idle_msg", this.value);
			});
		},

		get_data: function(key) {
			return _get_data(key);
		},

		set_data: function(key, value) {
			_set_data(key, value);
		}
	}
}());

HarvestMood.init();

