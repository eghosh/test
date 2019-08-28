
n = 4
#global a = rand(n,n)
#global a = hcat(a,a)

#a = [0.713447 0.351795 0.193486 0.713447 0.351795 0.193486; 0.487274 0.117371 0.407699 0.487274 0.117371 0.407699; 0.815415 0.408276 0.339959 0.815415 0.408276 0.339959]
a =[0.932525 0.53321 0.591048 0.39235 0.932525 0.53321 0.591048 0.39235; 0.00481761 0.343565 0.379658 0.304636 0.00481761 0.343565 0.379658 0.304636; 0.13668 0.384012 0.175796 0.556526 0.13668 0.384012 0.175796 0.556526; 0.630523 0.536769 0.992816 0.59428 0.630523 0.536769 0.992816 0.59428]
m = size(a, 2)

startcol = 0
whole1 = 0
for i = 1:n  #grouping loop
    global startcol = startcol +1
    k = startcol
    group = 1
    for j = 1:n
        group = group * a[j,k]
        println(j,k)
        k = k + 1
    end
    global whole1 = whole1 + group
end
println(whole1)

#y = [0]
#for x = 0:(m-1)
#    global y = hcat(y,m-x)
#end
#y = y[:,2:size(y,2)]

startcol = m + 1
whole2 = 0
for i = 1:n
    global startcol = startcol - 1
    k = startcol
    group = 1
    for j = 1:n
        group = group * a[j,k]
        println(j,k)
        k = k - 1
    end
    global whole2 = whole2 + group
end
println(whole2)

det = whole1 - whole2
println(det)

println("end")
