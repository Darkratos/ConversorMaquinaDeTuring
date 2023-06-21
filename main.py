import xml.etree.ElementTree as ET

mytree = ET.parse( 'input.jff' )

root = mytree.getroot( )
automato = root.find( 'automaton' )

name = "Count verification of a's, b's and c's\n"
initial = []
accept = []
buffer = ''

for x in automato.findall( 'state' ):  
   if x.findall( 'initial' ):
      initial.append( x.attrib[ 'name' ] )

   if x.findall( 'final' ):
      accept.append( x.attrib[ 'name' ] )

buffer += f'name: { name }\ninit: { ",".join( initial ) }\naccept: { ",".join( accept ) }\n\n'

for x in automato.findall( 'transition' ):
   fr = x.find( 'from' ).text
   to = x.find( 'to' ).text
   rd = x.find( 'read' ).text
   wr = x.find( 'write' ).text
   mv = x.find( 'move' ).text

   buffer += 'q' + fr + ', ' + ( rd if rd else '_' ) + '\n'
   buffer += 'q' + to + ', ' + ( wr if wr else '_' ) + ', ' + ( '<' if mv == 'L' else '>' ) + '\n'

   buffer += '\n'

print( buffer )

with open('./output.txt', 'w') as file:
   file.write( buffer )