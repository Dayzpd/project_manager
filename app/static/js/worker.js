function display_projects(){
  $.getJSON('/projects/get', function(response){
    var html = '<div class="card-deck">' +
                '<div class="card">' +
                '<div class="card-body">' +
                '<h3 class="card-title">Projects</h3>' +
                '<div class="table-responsive">' +
                '<table class="table" class="table-responsive">' +
                '<thead>' +
                '<tr>' +
                '<th scope="col">Name</th>' +
                '<th scope="col">Repository</th>' +
                '<th scope="col">Port</th>' +
                '<th scope="col">Action</th>' +
                '</tr>' +
                '</thead>' +
                '<tbody id="projects_table">';
    $.each(response['data'], function(index, project){
      html += '<tr name="name" id=' + project['name'] + '>' +
              '<td style="width:20%;">' + project['name'] + '</td>' +
              '<td style="width:45%;">' + project['repo_link'] + '</td>' +
              '<td style="width:20%;">' + project['port'] + '</td>' +
              '<td style="width:15%;"><span class="btn-floating btn-sm"><i style="color:red;" class="fas fa-trash-alt"></i></span></td>' +
              '</tr>';
    });
    html += '<form id="add_project_form">' +
            '<tr>' +
            '<td style="width:20%;"><input class="form-control" placeholder="Name" type="text" name="name"></td>' +
            '<td style="width:40%;"><input class="form-control" placeholder="Reposity Link" type="url" name="repo_link"></td>' +
            '<td style="width:25%;"><input class="form-control" placeholder="Port" type="integer" name="port"></td>' +
            '<td style="width:15%;"><span id="add_project" class="btn-floating btn-sm"><i style="color:green;" class="fas fa-plus-square"></i></span></td>' +
            '</tr>' +
            '</form>' +
            '</tbody>' +
            '</table>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>';
    $('#body').append(html);
  });
}

$(document).on('click', '#add_project', function() {
  alert('clicked');
  var name = $('input[type=text][name=name]').val();
  var repo_link = $('input[type=url][name=repo_link]').val();
  var port = $('input[type=integer][name=port]').val();
  var form = {
    'name': name,
    'repo_link': repo_link,
    'port': port
  }
  $.post('/projects/put', form, function(data){
      alert(data);
  });
  display_projects()
});

$(document).on('click', 'tr[name="name"]', function() {
  $.post('/projects/get', {'name': this.id}, function(response){
    var html = '<div class="card-deck">' +
               '<div class="card">' +
               '<div class="card-body">' +
               '<h3 id="project_name" class="card-title"></h3>' +
               '<div class="card-text">' +
               '<h5 id="name" name="' + response['data'][0]['name'] + '">Name: ' + response['data'][0]['name'] + '</h5><br />' +
               '<h5>Reposity: ' + response['data'][0]['repo_link'] + '</h5><br />' +
               '<h5>Port: ' + response['data'][0]['port'] + '</h5><br />' +
               '<div class="btn-toolbar" role="toolbar">' +
               '<div class="btn-group mr-2" role="group">' +
               '<button name="shell" id="pull" type="button" class="btn btn-default">Pull</button>' +
               '<button name="shell" id="build" type="button" class="btn btn-default">Build</button>' +
               '<button name="shell" id="run" type="button" class="btn btn-default">Run</button>' +
               '<button name="shell" id="stop" type="button" class="btn btn-default">Stop</button>' +
               '<button name="shell" id="remove" type="button" class="btn btn-default">Remove</button>' +
               '</div>' +
               '</div>' +
               '</div>' +
               '</div>' +
               '</div>' +
               '</div>';
    $('#body').html(html);
  });
});

$(document).on('click', 'button[name="shell"]', function() {
  var action = this.id;
  var name = $('#name').attr('name');
  var data = {
    'name': name,
    'action': action
  }
  $.post('/shell', data, function(response){
    alert(response);
  });
});

$(document).ready(function() {
  display_projects()
});
