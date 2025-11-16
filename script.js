document.addEventListener('DOMContentLoaded', () => {
  window.editStudent = function(id, idno, lastname, firstname, course, level) {
    document.getElementById('id').value = id;
    document.getElementById('idno').value = idno;
    document.getElementById('lastname').value = lastname;
    document.getElementById('firstname').value = firstname;
    document.getElementById('course').value = course;
    document.getElementById('level').value = level;
  };

  window.deleteStudent = function(id) {
    if (confirm("Are you sure you want to delete this student?")) {
      fetch(`/delete/${id}`, { method: "POST" })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            document.getElementById(`student-${id}`).remove();
          } else {
            alert("Failed to delete student.");
          }
        });
    }
  };

  window.clearForm = function() {
    document.getElementById('studentForm').reset();
    document.getElementById('id').value = '';
  };


  const profileImageInput = document.getElementById('profileImageInput');
  const profilePreview = document.getElementById('profilePreview');

  if (profileImageInput && profilePreview) {
    profileImageInput.addEventListener('change', function() {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          profilePreview.src = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    });
  }
});
