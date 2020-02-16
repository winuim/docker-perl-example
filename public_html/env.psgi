use strict;
use warnings;

my $app = sub {
    my $env = shift;

    my $content = << "END_OF_HTML";
<ul>
@{[ map { "<li>$_: $env->{$_}</li>" } keys %{$env} ]}
</ul>
END_OF_HTML

    [ 200, [ "Content-Type", "text/html" ], [ $content ] ];
};
