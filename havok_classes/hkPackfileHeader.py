

class hkPackfileHeader(object):
	magic: int
	userTag: int
	fileVersion: int
	layoutRules: int
	numSections: int
	contentsSectionIndex: int
	contentsSectionOffset: int
	contentsClassNameSectionIndex: int
	contentsClassNameSectionOffset: int
	contentsVersion: str
	flags: int
	maxpredicate: int
	predicateArraySizePlusPadding: int
