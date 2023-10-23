is_triangle(Angle1, Angle2, Angle3) :-
    Angle1 > 0, Angle2 > 0, Angle3 > 0,
    Total is Angle1 + Angle2 + Angle3,
    Total =:= 180.

is_right_triangle(Angle1, Angle2, Angle3) :-
    member(90, [Angle1, Angle2, Angle3]).

main :-
    write('Enter the three angles of the triangle: '),
    read(Angle1),
    read(Angle2),
    read(Angle3),
    
    (is_triangle(Angle1, Angle2, Angle3) ->
        writeln('These angles form a valid triangle.'),
        (is_right_triangle(Angle1, Angle2, Angle3) ->
            writeln(' It is also a right triangle.');
            writeln(' It is not a right triangle.')
        );
        write('These angles do not form a valid triangle.')
    ).

:- initialization(main).
