'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var shell = require('gulp-shell')
var watch = require('gulp-watch');
var webserver = require('gulp-webserver');
var portscanner = require('portscanner');


gulp.task('webserver', ['build'], function() {
  // Find the first available port. Asynchronously checks, so first port
  // determined as available is returned.
  portscanner.findAPortNotInUse(8000, 8020, '127.0.0.1', function(error, port) {
    // console.log('AVAILABLE PORT AT: ' + port)
    gulp.src('.')
      .pipe(webserver({
        port:port,
        livereload: false,
        directoryListing: false,
        open: false,
        fallback: 'build/index.html'
      }));

  })
});

gulp.task('scss', function () {
  gulp.src('./assets/css/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./assets/css/dist'));
});

gulp.task('build-css', ['build'], function(){
    gulp.src('./build/styles.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(gulp.dest('./build/'));
  }
);

gulp.task('build',shell.task(
  ['./bin/build.py']
));

// default gulp task
gulp.task('default', ['webserver', 'scss', 'build-css'], function() {
  gulp.watch('./assets/css/**/*.scss', ['scss']);
  gulp.watch(['bin/build.py', './pages/*', './templates/*.tpl.html'], ['build-css']);
});
