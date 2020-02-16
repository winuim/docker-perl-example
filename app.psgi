use Plack::Builder;
use Plack::App::WrapCGI;
use Plack::App::File;

my $app = sub {
    my $env = shift;

    my $content = << "END_OF_HTML";
<ul>
@{[ map { "<li>$_: $env->{$_}</li>" } keys %{$env} ]}
</ul>
END_OF_HTML

    [ 200, [ "Content-Type", "text/html" ], [ $content ] ];
};

builder {
    mount "/" => Plack::App::WrapCGI->new(script => './public_html/test.cgi', execute => 1)->to_app;
    mount "/css" => Plack::App::File->new(root => './public_html/css')->to_app;
    mount "/env" => $app;
};
