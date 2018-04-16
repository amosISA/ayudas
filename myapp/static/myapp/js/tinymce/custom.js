tinymce.init({
    selector: 'textarea#id_comentarios',
    height: 238,
    menubar: false,
    plugins: [
      'advlist autolink lists link image charmap print preview anchor textcolor',
      'searchreplace visualblocks code fullscreen',
      'insertdatetime media table contextmenu paste code help',
      'paste'
    ],
    paste_as_text: true,
    toolbar: 'insert | undo redo |  styleselect | bullist numlist outdent indent | removeformat | help | emoticons',
    content_css: [
      '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css']
});