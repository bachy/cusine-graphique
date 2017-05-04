'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var shell = require('gulp-shell')
var watch = require('gulp-watch');
var webserver = require('gulp-webserver');

gulp.task('webserver', function() {
  gulp.src('.')
    .pipe(webserver({
      livereload: false,
      directoryListing: false,
      open: false,
      fallback: 'index.html'
    }));
});

gulp.task('scss', function () {
  gulp.src('./assets/css/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./assets/css/dist'));
});


// default gulp task
gulp.task('default', ['webserver', 'scss'], function() {
  gulp.watch('./assets/css/**/*.scss', ['scss']);
});
