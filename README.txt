#annotator_ID - unique identifier for an annotator_ID

#text_ID - unique identifier for the instance being annotated

#version - the version of stimuli given to the annotator
flat_spr - Annotator was exposed to a pre-determined number of instances in a spreadsheet and used separate definition file to designate instances
flat_gui -  Annotator was exposed to a gui and given flat categories
tier_gui - Annotator was exposed to a gui showing a hierarchical annotation scheme
slid_gui - Annotator was exposed to a gui showing hierarchical annotation scheme and sliders to indicate dimensions on a continuum

#annotator_grp - the 'experimental' group that annotator belongs to
ugr - undergrad
5yr - undergrad/master
grd - grad student
crwd - crowdworker
ukn - unknown

#text - the annotated text

#multi_lab - label for multi-class experiments
In cases where more than one designation exists:
Hate> offensive > explicit > implicit > counterspeech > casual profanity > argumentative > not enough information 
NAB - non-abusive
AR - argumentative
PR - casual profanity
CS - counter speech
O - offensive
I - implicitly abusive
E - explicitly abusive
H - Hate
NEI - Not enough information

#second_lab - secondary labels for cases in which more than one label is available

#binary_lab - binary label assignment based on multi-labels
Hate, offensive, implicit/explicit = 1 = abusive
counterspeech, casual profanity, argumentative = 0 = non-abusive
not enough information = nei

#target - text description of target by annotators

#target_lab - category for text descriptions by annotators
