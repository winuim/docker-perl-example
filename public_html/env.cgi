#!/usr/local/bin/perl

use strict;
use warnings;

use Plack::Loader;
my $app = Plack::Util::load_psgi("./env.psgi");
Plack::Loader->auto(port => 5000)->run($app);
