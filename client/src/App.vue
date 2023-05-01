<template>
    <div class="w-screen min-h-screen bg-neutral-900 text-neutral-300">
        <header class="w-full h-[60px] bg-neutral-950 flex items-center justify-center">
            <h2 class="text-2xl font-bold">Math Rebus</h2>
        </header>
        <div class="container">
            <div class="border border-neutral-300 p-5 rounded flex mt-5 justify-between flex-col">
                <h2 class=" text-2xl font-bold">Как это работает?</h2>
                <p>Составьте уравнение и получите его решение!</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 mt-4 justify-center">
                    <div class="flex items-center bg-neutral-800 my-2 mx-2 py-2 justify-center">
                        <div class="flex flex-col items-end relative">
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">К</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">О</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">З</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">А</p>
                            </div>
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">К</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">О</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">З</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">А</p>
                            </div>
                            <div class="flex pt-1 border-t-2 border-neutral-300">
                                <p class="bg-neutral-700 rounded p-1">C</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Т</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">А</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Д</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">О</p>
                            </div>
                            <p class="bg-neutral-700 rounded p-1 absolute top-[16px] left-[0px]">+</p>
                        </div>
                        <div>
                            <p class="text-6xl mb-4 mx-6">=></p>
                        </div>
                        <div class="flex flex-col items-end relative">
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">8</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">5</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">3</p>
                            </div>
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">8</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">5</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">3</p>
                            </div>
                            <div class="flex pt-1 border-t-2 border-neutral-300">
                                <p class="bg-neutral-700 rounded p-1">1</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">7</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">3</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">0</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                            </div>
                            <p class="bg-neutral-700 rounded p-1 absolute top-[16px] left-[0px]">+</p>
                        </div>
                    </div>
                    <div class="flex items-center bg-neutral-800 my-2 mx-2 py-2 justify-center">
                        <div class="flex flex-col items-end relative ml-4">
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">Т</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">О</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Р</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Г</p>
                            </div>
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">Г</p>
                            </div>
                            <div class="flex pt-1 border-t-2 border-neutral-300">
                                <p class="bg-neutral-700 rounded p-1">Г</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Р</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">О</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">Т</p>
                            </div>
                            <p class="bg-neutral-700 rounded p-1 absolute top-[16px] left-[-18px]">*</p>
                        </div>
                        <div>
                            <p class="text-6xl mb-4 mx-12">=></p>
                        </div>
                        <div class="flex flex-col items-end relative ml-4">
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">1</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">0</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">8</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">9</p>
                            </div>
                            <div class="flex mb-1">
                                <p class="bg-neutral-700 rounded p-1">9</p>
                            </div>
                            <div class="flex pt-1 border-t-2 border-neutral-300">
                                <p class="bg-neutral-700 rounded p-1">9</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">8</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">0</p>
                                <p class="bg-neutral-700 rounded p-1 ml-1">1</p>
                            </div>
                            <p class="bg-neutral-700 rounded p-1 absolute top-[16px] left-[-18px]">*</p>
                        </div>
                    </div>
                    <div class="flex items-center bg-neutral-800 my-2 mx-2 py-2 lg:border-none flex-col ">
                        <div class="flex">
                            <p class="bg-neutral-700 rounded p-1">А</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">+</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">Б</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">*</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">(</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">А</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">+</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">С</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">)</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">-</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">Б</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">=</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">А</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">Б</p>
                        </div>
                        <div>
                            <p class="text-2xl rotate-90 font-bold my-2">=></p>
                        </div>
                        <div class="flex">
                            <p class="bg-neutral-700 rounded p-1">2</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">+</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">*</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">(</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">2</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">+</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">3</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">)</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">-</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">=</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">2</p>
                            <p class="bg-neutral-700 rounded p-1 ml-1">6</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="border border-neutral-300 p-5 rounded flex flex-col mt-5 justify-between">
                <form @submit.prevent="submit" class="flex flex-wrap gap-y-3 items-center">
                    <div class="">
                        <input
                            type="text"
                            v-model="left"
                            class="rounded bg-neutral-700 w-[300px] px-3"
                        >
                    </div>
                    <div class="flex">
                        <p class="rounded p-1 mx-4">=</p>
                        <input
                            type="text"
                            v-model="right"
                            class="rounded bg-neutral-700 w-[150px] px-3"
                        >
                    </div>
                    <button class="border-2 font-bold border-emerald-800 rounded px-2 py-1 ml-4 w-fit">Проверить решение</button>
                </form>
                <h4 class="text-red-400">{{ error }}</h4>
                <br>
                <div v-if="answers.length">
                    <h2 class="font-bold text-2xl">Возможные решения:</h2>
                    <p class="text-lg flex flex-wrap" v-for="answer in answers"><span>{{answer}}</span> : <span class="ml-4">{{ matchLetter(answer) }}</span></p>
                </div>
                <div v-else class="bold text-xl mt-8">
                    <p>Уравение может содержать буквы, цифры, операторы <b>+</b> <b>-</b> <b>*</b> и круглые скобки.</p>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
import {computed, ref, watch} from 'vue'

const left = ref('')
const right = ref('')
const answers = ref([])
const fullStr = ref('')

const error = ref('')

watch(left, (value)=>{
    error.value = ''
    left.value = value.replaceAll(' ', '').toUpperCase()
})

watch(right, (value)=>{
    right.value = value.replaceAll(' ', '').toUpperCase()
})

async function submit() {
    const url = 'https://functions.yandexcloud.net/d4e5d2hv9men8ljebv79';

    answers.value = []
    function test_valid(){
        const reg = /^([А-ЯA-Z\d()+*-])+$/
        return reg.test(right.value) && reg.test(left.value)
    }

    if(!left.value.length && !right.value.length){
        error.value = 'Задайте выражение' 
        return
    }

    if(!left.value.length){
        error.value = 'Левая часть выражения не задана' 
        return
    }

    if(!right.value.length){
        error.value = 'Правая часть выражения не задана' 
        return
    }

    if(!test_valid()){
        error.value = 'Обнаружены неразрешенные символы' 
        return
    }

    if(left.value == right.value){
        error.value = 'Выражения слева и справа идентичны'
        return
    }
    

    fullStr.value = left.value + ' = ' + right.value

    const response = await fetch(url, {
        method: 'POST',
        body: fullStr.value
    });
    try{
        const answerResponse = await response.json();
        answers.value = [...answerResponse.answer]
        if(answers.value.length == 0){
            error.value = 'Нет решений'
        }else{
            error.value = ''
        }
    }catch{
        error.value = 'Сервер недоступен'
    }
}

function matchLetter(answer) {
    let str = fullStr.value
    let matchList = {}
    str.split('').forEach((el,i) => {
        if(!matchList.hasOwnProperty(el) && /^[A-ZА-Я]+$/.test(el)) {
            matchList[el] = answer[i]
        }
    })
    let matchStr = ''
    for (const property in matchList) {
        matchStr += `${property} => ${matchList[property]}; `;
    }
    return matchStr
}
</script>
<style>
.container {
    margin: 0 auto;
    max-width: 1280px;
    padding: 10px;
}
input {
    outline: none;
    height: 30px;
    text-transform: uppercase;
}
p {
    cursor: default;
}
</style>