from collections import namedtuple

def read_graphs( file_path ):

    with open( file_path , 'r' ) as f:

        k = int( f.read() )
        for i in range( k ):

            V = set()
            E = dict()

            m , n = map( int( f.read().split() ) )
            for j in range( m ):

                u , v , w = map( int( f.read().split() ) )
                E[ ( u , v ) ] = w
                V = V | set( [ u , v ] )
            
            yield V , E

node_tuple = namedtuple( "node" , [ "val" , "parent" , "flow" ] ) 

def choke_point_relax( u , v , w ):

    flow_val = min( u.flow , w( u , v ) )
    if flow_val > v.flow:
        v.flow = flow_val
        v.parent = u

def chokepoint_dijkstra( V , E , s , t ):
    '''
        Achar o caminho de maior gargalo entre os nos
        s e t no Grafo valorado e direcionado ( V , E )
    '''
    pass

def max_flow( V , E , s , t ):

    flow = 0;
    residual_E = E.copy()
    flow_values = { tup:0 for tup in E }

    while True:

        path = chokepoint_dijkstra( V , residual_E , s , t )
        if not path:
            return flow , flow_values

        #--------------------------------------------------
        # Achando o gargalo
        path_edges = list( zip ( path[ : -1 ] , path[ 1: ] ) )
        choke_point = min( path_edges, key = lambda x : residual_E[ x ])
        choke_value = residual_E[ choke_point ]
        
        flow += choke_value
        for tup in path_edges:

            #--------------------------------------------------
            # Atualizando os fluxos no grafo original
            flow_values[ tup ] += choke_value

            #--------------------------------------------------
            # Atualizando o residual
            residual_E[ tup ] -= choke_value
            if residual_E[ tup ] == 0:
                    del residual_E[ tup ]

