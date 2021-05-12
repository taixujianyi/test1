

#use Pex::Text

sub PatternCreate {
	my ($length) = @_;
	my ($X,$Y,$z);
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
	

print PatternCreate(2000);
#print Pex::Text::PatternCreate(2000);	
