
#use Pex::Text
#use utf8;
#binmode STDIN, ":utf8";
#binmode STDOUT, ":ut8";
#use strict;
use warnings;
#my ($length,$addr) = (0,0);
#my $length;
#my $addr;
sub PatternCreate {
	my ($length)=@_;
	my ($X,$Y,$Z);
	my $res;

	while (1)
	{
		for my $X("A" .. "Z") { for my $Y("a" .. "z") { for my $Z(0 .. 9) {
			$res .=$X;
			return $res if length($res) >= $length;
			
			$res .=$Y;
			return $res if length($res) >= $length;
			
			$res .=$Z;
			return $res if length($res) >= $length;
			}}}
	}
}

sub PatternOffset{
	#my $pattern1 = PatternCreate(shift);
	my $pattern = shift;
	my $address = shift;
	my $endian = @_?shift():'V';
	my @results;
	my ($idx,$lst) = (0,0);
	
	$address = pack($endian,hex($address));
	$idx = index($pattern,$address,$lst);#在这里你把“,”不小心打成了“，”。不是中文
	
	while ($idx>0)
	{
		push @results,$idx;
		$lst = $idx + 1;
		$idx = index($pattern,$address,$lst);
	}
	return @results;
}

#print join(',',Pex::Text::PatternOffset(Pex::Text::PatternCreate($length),$addr))."\n";

print join(',',PatternOffset(PatternCreate(2000),68423768))."\n";
#print join(',',PatternOffset(PatternCreate($length),$addr))."\n";#cmd传参不会

