use warnings;
use strict;

my $a = 1;
my $b = 2.2;


sub calc_sum {
  my ( $a, $b ) = @_;
  return $a + $b;
}

print( calc_sum( $a, $b ) )
