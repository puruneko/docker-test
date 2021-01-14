FROM nginx
#nginx.confで定義されるhtmlホスティングディレクトリにホストのhtmlフォルダをコピーする
COPY ./index.html /usr/share/nginx/html/
#nginx設定ファイルをカスタムコンフィグフォルダにコピーする
COPY ./mynginx.conf /etc/nginx/conf.d/default.conf
